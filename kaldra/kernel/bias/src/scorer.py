import joblib
from pathlib import Path
import numpy as np

# --- Model Loading ---
BIAS_KERNEL_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BIAS_KERNEL_DIR / "data" / "model_v02.joblib"

def _load_model():
    """
    Tries to load the trained model from disk.
    Returns the model object or None if it doesn't exist.
    """
    try:
        model = joblib.load(MODEL_PATH)
        print("Scoring model 'model_v02.joblib' loaded successfully.")
        return model
    except FileNotFoundError:
        print("Warning: Model file not found. Falling back to v0.1 heuristic.")
        return None

MODEL = _load_model()

def compute_bias_score(delta12: list[float]) -> tuple[float, str]:
    """
    Computes a bias score and determines a label from a 12-dimensional vector.

    If a trained model (`model_v02.joblib`) is available, it is used to
    predict the probability of the 'biased' class.

    If the model is not found, it falls back to a simple v0.1 heuristic.
    """
    if not isinstance(delta12, list) or len(delta12) != 12:
        raise ValueError("Input must be a 12-element list of floats.")

    if MODEL:
        # --- v0.2 Logic: Use the trained model ---
        # The model expects a 2D array, so we reshape the input
        delta12_reshaped = np.array(delta12).reshape(1, -1)

        # Predict the probability of each class: [P(neutral), P(biased)]
        probabilities = MODEL.predict_proba(delta12_reshaped)

        # The bias_score is the probability of the 'biased' class
        # We find the index of the 'biased' class in the model's learned classes
        biased_class_index = np.where(MODEL.classes_ == 'biased')[0][0]
        bias_score = probabilities[0, biased_class_index]

    else:
        # --- v0.1 Fallback Logic: Heuristic ---
        bias_score = 1.0 - delta12[0]

    # Determine the label based on a simple 0.5 threshold
    label = "biased" if bias_score >= 0.5 else "neutral"

    return float(bias_score), label
