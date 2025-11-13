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

# --- Pre-load metadata ---
def _load_archetype_meta():
    """Loads and sorts the archetype metadata for easy indexing."""
    data_path = Path(__file__).resolve().parent.parent / "data" / "archetypes" / "delta12_archetypes.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Sort by ID to ensure the list index corresponds to (id - 1)
    return sorted(data, key=lambda x: x["id"])

DELTA12_META = _load_archetype_meta()


def analyze_text(text: str, locale: str = "pt-BR") -> dict:
    """
    Runs the full KALDRA-Bias analysis pipeline on a given text.
    """
    # 1. Generate text embedding
    embedding = get_embedding(text)

    # 2. Project to 12-dimensional archetypal space
    delta12_vector = project_to_delta12(embedding)

    # 3. Apply cultural modulation
    delta12_modulated, plan = apply_kindra(delta12_vector, locale)

    # 4. Apply the τ-layer (doubt policy)
    tau_result = apply_tau_policy(delta12_modulated)

    # 5. Handle inconclusive cases
    if tau_result["status"] == "inconclusive":
        explanation, dominant_archetype = build_explanation(delta12_modulated, "inconclusive", None)
        return {
            "bias_score": None,
            "label": "inconclusive",
            "confidence": tau_result["confidence"],
            "dominant_archetype": dominant_archetype,
            "plan": plan,
            "explanation": explanation
        }

    # 6. If proceeding, compute bias score
    bias_score, label = compute_bias_score(delta12_modulated)

    # 7. Determine dominant archetype and build explanation
    explanation, dominant_archetype = build_explanation(delta12_modulated, label, bias_score)

    # 8. Assemble the final response dictionary
    analysis_result = {
        "bias_score": bias_score,
        "label": label,
        "confidence": tau_result["confidence"],
        "dominant_archetype": dominant_archetype,
        "plan": plan,
        "explanation": explanation
    }

    return analysis_result
