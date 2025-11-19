import pandas as pd
import sys
from pathlib import Path
from sklearn.metrics import accuracy_score, precision_score, recall_score

# --- Setup Paths ---
# Add the 'kaldra/kernel/safeguard' directory to the Python path.
# This allows the 'src' module to be imported as a package.
EVAL_DIR = Path(__file__).parent.resolve()
BIAS_KERNEL_DIR = EVAL_DIR.parent
sys.path.append(str(BIAS_KERNEL_DIR))

from src.pipeline import analyze_text

# --- Constants ---
DATA_DIR = BIAS_KERNEL_DIR / "data" / "datasets"
GOLD_CSV_PATH = DATA_DIR / "gold.csv"
PREDS_CSV_PATH = DATA_DIR / "preds.csv"

def run_evaluation():
    """
    Main function to run the evaluation pipeline.
    """
    # 1. Load the gold standard dataset
    try:
        gold_df = pd.read_csv(GOLD_CSV_PATH)
    except FileNotFoundError:
        print(f"Error: Gold standard file not found at {GOLD_CSV_PATH}")
        return

    # 2. Get predictions for each text
    predictions = []
    print("Running analysis on gold standard dataset...")
    for index, row in gold_df.iterrows():
        text = row["text"]
        result = analyze_text(text)
        predictions.append({
            "text": text,
            "pred_label": result["label"],
            "bias_score": result["bias_score"]
        })
    print("Analysis complete.")

    # 3. Save predictions to preds.csv
    preds_df = pd.DataFrame(predictions)
    preds_df.to_csv(PREDS_CSV_PATH, index=False)
    print(f"Predictions saved to {PREDS_CSV_PATH}")

    # --- 4. Calculate Metrics ---
    eval_df = pd.merge(gold_df, preds_df, on="text")
    conclusive_df = eval_df[eval_df["pred_label"] != "inconclusive"].copy()

    if conclusive_df.empty:
        print("\nNo conclusive predictions were made. Cannot calculate metrics.")
        return

    y_true = conclusive_df["label"]
    y_pred = conclusive_df["pred_label"]

    accuracy = accuracy_score(y_true, y_pred)
    precision_biased = precision_score(y_true, y_pred, pos_label="biased", zero_division=0)
    recall_biased = recall_score(y_true, y_pred, pos_label="biased", zero_division=0)

    # 5. Print the results
    print("\n--- Evaluation Metrics ---")
    print(f"Accuracy:  {accuracy:.2f}")
    print(f"Precision (biased): {precision_biased:.2f}")
    print(f"Recall (biased):    {recall_biased:.2f}")
    print("--------------------------")

if __name__ == "__main__":
    run_evaluation()
