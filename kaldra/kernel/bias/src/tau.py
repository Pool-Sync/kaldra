import numpy as np
from typing import Dict, List

def estimate_confidence(delta12: List[float]) -> float:
    """
    A simple heuristic for estimating confidence based on the distribution of the
    delta12 vector. The core idea is that a more concentrated (less uniform)
    distribution implies higher confidence in the archetypal projection.

    The confidence is calculated as the difference between the maximum value and
    the mean value of the vector, roughly normalized to the [0, 1] range.
    """
    if not delta12:
        return 0.0

    arr = np.array(delta12, dtype=float)
    max_val = float(arr.max())
    mean_val = float(arr.mean())

    # Raw confidence is the spread between the peak and the average
    raw_confidence = max_val - mean_val

    # Simple normalization: multiply by a factor to scale the typical range.
    # Clip the value to ensure it stays within the [0, 1] bounds.
    confidence = max(0.0, min(1.0, raw_confidence * 10.0))

    return confidence

def apply_tau_policy(delta12: List[float], tau_threshold: float = 0.4) -> Dict:
    """
    Applies the τ-layer (doubt policy) to the analysis.

    This layer acts as a gatekeeper. If the confidence in the archetypal
    projection is too low (below the tau_threshold), it flags the result as
    'inconclusive'. Otherwise, it signals to 'proceed' with the rest of
    the analysis.

    Args:
        delta12: The 12-dimensional archetypal vector.
        tau_threshold: The confidence threshold below which the result is
                       deemed inconclusive.

    Returns:
        A dictionary containing the 'status' ('inconclusive' or 'proceed')
        and the calculated 'confidence'.
    """
    confidence = estimate_confidence(delta12)

    if confidence < tau_threshold:
        return {
            "status": "inconclusive",
            "confidence": confidence
        }

    return {
        "status": "proceed",
        "confidence": confidence
    }
