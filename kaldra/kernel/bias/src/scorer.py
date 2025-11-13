import os
import joblib
from pathlib import Path
import numpy as np

# --- Path Definitions ---
BIAS_KERNEL_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BIAS_KERNEL_DIR / "data"
MODEL_V04_PATH = DATA_DIR / "model_v04.joblib"
MODEL_V02_PATH = DATA_DIR / "model_v02.joblib"

# --- Simple Global Cache ---
MODEL_V04 = None
MODEL_V02 = None

def _load_model_v04():
    """Loads the v0.4 model if available and caches it."""
    global MODEL_V04
    if MODEL_V04 is None and MODEL_V04_PATH.exists():
        print("Loading scoring model v0.4...")
        MODEL_V04 = joblib.load(MODEL_V04_PATH)
    return MODEL_V04

def _load_model_v02():
    """Loads the v0.2 model if available and caches it."""
    global MODEL_V02
    if MODEL_V02 is None and MODEL_V02_PATH.exists():
        print("Loading scoring model v0.2...")
        MODEL_V02 = joblib.load(MODEL_V02_PATH)
    return MODEL_V02

# --- Initialize models on module load ---
_load_model_v04()
_load_model_v02()

def compute_bias_score(delta12: list[float]) -> tuple[float, str]:
    """
    Computes a bias score and determines a label from a 12-dimensional vector.

    It follows a priority-based fallback system:
    1. Tries to use the calibrated v0.4 model.
    2. If not found, falls back to the uncalibrated v0.2 model.
    3. If no model is found, falls back to the v0.1 heuristic.
    """
    if not isinstance(delta12, list) or len(delta12) != 12:
        raise ValueError("Input must be a 12-element list of floats.")

    X = np.array(delta12).reshape(1, -1)
    bias_score = 0.0

    if MODEL_V04:
        # --- v0.4 Logic: Calibrated Model ---
        # The model was trained on binary labels (0 for neutral, 1 for biased)
        # predict_proba returns [[P(class_0), P(class_1)]]
        proba_biased = MODEL_V04.predict_proba(X)[0, 1]
        bias_score = float(proba_biased)

    elif MODEL_V02:
        # --- v0.2 Logic: Uncalibrated Model ---
        probabilities = MODEL_V02.predict_proba(X)
        biased_class_index = np.where(MODEL_V02.classes_ == 'biased')[0][0]
        bias_score = probabilities[0, biased_class_index]

    else:
        # --- v0.1 Fallback Logic: Heuristic ---
        # This is kept for robustness if no model file is present
        if not np.isclose(sum(delta12), 1.0): # Heuristic assumes softmax output
             print("Warning: Heuristic fallback on non-normalized vector.")
        bias_score = 1.0 - delta12[0]

    # Determine the label based on the final score
    label = "biased" if bias_score >= 0.5 else "neutral"

    return float(bias_score), label
