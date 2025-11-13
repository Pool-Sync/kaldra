# --- Import necessary functions from other modules ---
from .embeddings import get_embedding
from .delta12 import project_to_delta12
from .kindra_3x48 import apply_kindra
from .scorer import compute_bias_score
from .tau import apply_tau_policy

def analyze_text(text: str, locale: str = "pt-BR") -> dict:
    """
    Runs the full KALDRA-Bias analysis pipeline on a given text.

    This function orchestrates the process:
    1. Generates text embedding.
    2. Projects to the 12-dimensional archetypal space (Δ12).
    3. Applies cultural modulation.
    4. Applies the τ-layer (doubt policy) to check for confidence.
    5. If confidence is sufficient, computes bias score and label.
    6. Assembles and returns the final analysis.
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
        return {
            "bias_score": None,
            "label": "inconclusive",
            "confidence": tau_result["confidence"],
            "dominant_archetype": "indefinido",
            "plan": plan,
            "explanation": "O sistema não tem confiança suficiente para emitir um julgamento."
        }

    # 6. If proceeding, compute bias score
    bias_score, label = compute_bias_score(delta12_modulated)

    # 7. Assemble the final response dictionary
    analysis_result = {
        "bias_score": bias_score,
        "label": label,
        "confidence": tau_result["confidence"],  # Use confidence from τ-layer
        "dominant_archetype": "placeholder",  # To be implemented
        "plan": plan,
        "explanation": "MVP placeholder explanation. Logic not yet implemented."
    }

    return analysis_result
