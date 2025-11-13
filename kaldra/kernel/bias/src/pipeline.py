import json
import numpy as np
from pathlib import Path
from typing import Optional

# --- Import necessary functions from other modules ---
from .embeddings import get_embedding
from .delta12 import project_to_delta12
from .kindra_3x48 import apply_kindra
from .scorer import compute_bias_score
from .tau import apply_tau_policy
from .explain import build_explanation_layers
from .delta144_mapping import map_to_delta144

# --- Pre-load metadata ---
def _load_archetype_meta():
    """Loads and sorts the archetype metadata for easy indexing."""
    data_path = Path(__file__).resolve().parent.parent / "data" / "archetypes" / "delta12_archetypes.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return sorted(data, key=lambda x: x["id"])

DELTA12_META = _load_archetype_meta()

# --- Helper Functions for Signals and Risk ---

def compute_signals(label: str, bias_score: Optional[float], confidence: float) -> dict:
    """Computes analytical signals based on the core results."""
    if bias_score is None:
        intensity = 0.0
        polarization = 0.0
    else:
        intensity = float(bias_score)
        polarization = float(bias_score * confidence)

    if label == "biased" and bias_score is not None and bias_score >= 0.7:
        emotion_hint = "raiva"
    elif label == "biased":
        emotion_hint = "tensão"
    elif label == "neutral":
        emotion_hint = "neutro"
    else:
        emotion_hint = "indefinido"

    return {
        "intensity": intensity,
        "polarization": polarization,
        "emotion_hint": emotion_hint,
        "attack_target": "indefinido" # Placeholder for future versions
    }

def compute_risk_level(label: str, bias_score: Optional[float], confidence: float) -> str:
    """Computes a simple risk level based on score and confidence."""
    if label == "inconclusive" or bias_score is None:
        return "indefinido"

    score = bias_score * confidence
    if score < 0.3:
        return "baixo"
    elif 0.3 <= score < 0.6:
        return "medio"
    else:
        return "alto"

# --- Main Analysis Pipeline ---

def analyze_text(text: str, locale: str = "pt-BR") -> dict:
    """
    Runs the full KALDRA-Bias analysis pipeline on a given text.
    """
    embedding = get_embedding(text)
    delta12_vector = project_to_delta12(embedding)
    delta12_modulated, plan = apply_kindra(delta12_vector, locale)
    tau_result = apply_tau_policy(delta12_modulated)
    confidence = tau_result["confidence"]

    dominant_index = np.argmax(delta12_modulated)
    dominant_archetype_name = DELTA12_META[dominant_index]["name"]
    delta144_info = map_to_delta144(dominant_archetype_name)

    if tau_result["status"] == "inconclusive":
        label = "inconclusive"
        bias_score = None
    else:
        bias_score, label = compute_bias_score(delta12_modulated)

    risk_level = compute_risk_level(label, bias_score, confidence)
    signals = compute_signals(label, bias_score, confidence)
    explanation_layers = build_explanation_layers(
        delta12_modulated, label, bias_score, confidence,
        dominant_archetype_name, delta144_info, plan
    )

    return {
        "bias_score": bias_score,
        "label": label,
        "confidence": confidence,
        "risk_level": risk_level,
        "dominant_archetype": dominant_archetype_name,
        "plan": plan,
        "archetype_detail": delta144_info,
        "explanation_layers": explanation_layers,
        "signals": signals,
    }
