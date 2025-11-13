import json
import numpy as np
from pathlib import Path

# --- Import necessary functions from other modules ---
from .embeddings import get_embedding
from .delta12 import project_to_delta12
from .kindra_3x48 import apply_kindra
from .scorer import compute_bias_score
from .tau import apply_tau_policy
from .explain import build_explanation
from .delta144_mapping import map_to_delta144

# --- Pre-load metadata ---
def _load_archetype_meta():
    """Loads and sorts the archetype metadata for easy indexing."""
    data_path = Path(__file__).resolve().parent.parent / "data" / "archetypes" / "delta12_archetypes.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return sorted(data, key=lambda x: x["id"])

DELTA12_META = _load_archetype_meta()

def analyze_text(text: str, locale: str = "pt-BR") -> dict:
    """
    Runs the full KALDRA-Bias analysis pipeline on a given text.
    """
    embedding = get_embedding(text)
    delta12_vector = project_to_delta12(embedding)
    delta12_modulated, plan = apply_kindra(delta12_vector, locale)
    tau_result = apply_tau_policy(delta12_modulated)

    explanation, dominant_archetype_name = build_explanation(
        delta12_modulated,
        "inconclusive" if tau_result["status"] == "inconclusive" else "",
        None
    )

    if tau_result["status"] == "inconclusive":
        return {
            "bias_score": None,
            "label": "inconclusive",
            "confidence": tau_result["confidence"],
            "dominant_archetype": dominant_archetype_name,
            "plan": plan,
            "explanation": explanation,
            "archetype_detail": map_to_delta144(dominant_archetype_name)
        }

    bias_score, label = compute_bias_score(delta12_modulated)
    explanation, dominant_archetype_name = build_explanation(delta12_modulated, label, bias_score)
    delta144_info = map_to_delta144(dominant_archetype_name)

    return {
        "bias_score": bias_score,
        "label": label,
        "confidence": tau_result["confidence"],
        "dominant_archetype": dominant_archetype_name,
        "plan": plan,
        "explanation": explanation,
        "archetype_detail": delta144_info
    }
