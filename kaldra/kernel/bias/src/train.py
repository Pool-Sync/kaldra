import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import accuracy_score, f1_score, matthews_corrcoef
import numpy as np

# Relative import from within the same package
from embeddings import get_embedding

# --- Define Paths ---
BIAS_KERNEL_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BIAS_KERNEL_DIR / "data"
DATASET_PATH = DATA_DIR / "datasets" / "bias_dataset_v04.csv"
MODEL_SAVE_PATH = DATA_DIR / "model_v04.joblib"

def train_calibrated_model_v04():
    """
    Main function to train, calibrate, and save the v0.4 model.
    """
    print("--- Starting Kaldra-Bias v0.4 Model Training ---")

    # 1. Load the new dataset
    try:
        df = pd.read_csv(DATASET_PATH)
        print(f"Loaded dataset: {DATASET_PATH} ({len(df)} rows)")
    except FileNotFoundError:
        print(f"Error: Dataset not found at {DATASET_PATH}. Aborting.")
        return

    # 2. Preprocess data
    # Filter out 'inconclusive' labels for supervised training
    df_supervised = df[df['label'].isin(['biased', 'neutral'])].copy()
    print(f"Filtered for supervised training: {len(df_supervised)} rows")

    # Convert labels to binary format (biased=1, neutral=0)
    df_supervised['label_binary'] = df_supervised['label'].apply(lambda x: 1 if x == 'biased' else 0)

    # 3. Generate embeddings (features)
    print("Generating text embeddings...")
    X = np.array([get_embedding(text) for text in df_supervised['text']])
    y = df_supervised['label_binary'].values
    print("Embeddings generated.")

    # 4. Split data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y  # Ensure label distribution is similar in both sets
    )
    print(f"Data split: {len(X_train)} training samples, {len(X_val)} validation samples.")

    # 5. Train the base Logistic Regression model
    print("Training base Logistic Regression model...")
    model = LogisticRegression(
        class_weight="balanced",  # Crucial for imbalanced datasets
        max_iter=500,
        C=1.0,
        random_state=42
    )
    model.fit(X_train, y_train)
    print("Base model training complete.")

    # 6. Calibrate the model using Platt scaling (sigmoid)
    print("Calibrating model probabilities...")
    # CalibratedClassifierCV uses cross-validation to fit the calibrator
    calibrated_model = CalibratedClassifierCV(model, method="sigmoid", cv=3)
    calibrated_model.fit(X_train, y_train)
    print("Calibration complete.")

    # 7. Evaluate the calibrated model on the validation set
    print("\n--- Evaluating Calibrated Model on Validation Set ---")
    y_pred = calibrated_model.predict(X_val)

    accuracy = accuracy_score(y_val, y_pred)
    f1 = f1_score(y_val, y_pred, zero_division=0)
    mcc = matthews_corrcoef(y_val, y_pred)

    print(f"Validation Accuracy: {accuracy:.4f}")
    print(f"Validation F1-Score: {f1:.4f}")
    print(f"Validation MCC:      {mcc:.4f}")
    print("--------------------------------------------------")

    # 8. Save the final calibrated model
    joblib.dump(calibrated_model, MODEL_SAVE_PATH)
    print(f"\nCalibrated model v0.4 successfully saved to: {MODEL_SAVE_PATH}")
    print("--- Training Process Finished ---")

if __name__ == "__main__":
    train_calibrated_model_v04()
