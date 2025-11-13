import pandas as pd
import joblib
from pathlib import Path
from sklearn.linear_model import LogisticRegression

# Since this script is in `src`, we can do a relative import
from embeddings import get_embedding

# --- Define Paths ---
# The script is in `src`, so we navigate up one level to the `bias` directory
BIAS_KERNEL_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BIAS_KERNEL_DIR / "data"
DATASET_PATH = DATA_DIR / "datasets" / "gold.csv"
MODEL_SAVE_PATH = DATA_DIR / "model_v02.joblib"

def train_and_save_model():
    """
    Loads the gold standard dataset, trains a logistic regression model,
    and saves it to a file.
    """
    print("--- Starting Model Training ---")

    # 1. Load the dataset
    try:
        df = pd.read_csv(DATASET_PATH)
        print(f"Successfully loaded {DATASET_PATH} with {len(df)} records.")
    except FileNotFoundError:
        print(f"Error: Dataset not found at {DATASET_PATH}. Aborting training.")
        return

    # 2. Generate embeddings for each text (features X)
    print("Generating embeddings for the training data...")
    X = [get_embedding(text) for text in df['text']]

    # 3. Get the labels (target y)
    y = df['label']
    print("Embeddings generated and labels prepared.")

    # 4. Train a logistic regression model
    print("Training Logistic Regression model...")
    model = LogisticRegression(random_state=42)
    model.fit(X, y)
    print("Model training complete.")

    # 5. Save the trained model
    # Ensure the parent directory exists
    MODEL_SAVE_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_SAVE_PATH)
    print(f"Model successfully saved to: {MODEL_SAVE_PATH}")
    print("-----------------------------")

if __name__ == "__main__":
    train_and_save_model()
