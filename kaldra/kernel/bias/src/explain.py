import json
import numpy as np
from pathlib import Path
from typing import List, Optional

# --- Constants and Data Loading ---
DATA_PATH = Path(__file__).parent.parent / "data" / "archetypes"
ARCHETYPES_PATH = DATA_PATH / "delta12_archetypes.json"

def _load_archetypes():
    """Loads the archetype names from the JSON file."""
    with open(ARCHETYPES_PATH, "r", encoding="utf-8") as f:
        archetypes_data = json.load(f)
    # Create a simple list of names, assuming IDs are ordered 1-12
    return [item["name"] for item in sorted(archetypes_data, key=lambda x: x["id"])]

ARCHETYPE_NAMES = _load_archetypes()

# --- Main Function ---

def build_explanation(
    delta12: List[float],
    label: str,
    bias_score: Optional[float]
) -> tuple[str, str]:
    """
    Builds a simple, human-readable explanation for the analysis result.

    This v0.1 implementation identifies the dominant archetype and constructs
    a template-based explanation based on the final label.

    Args:
        delta12: The 12-dimensional archetypal vector.
        label: The final classification label ('inconclusive', 'neutral', 'biased').
        bias_score: The calculated bias score, which can be None for inconclusive results.

    Returns:
        A tuple containing:
        - The generated explanation string.
        - The name of the dominant archetype.
    """
    # 1. Handle the inconclusive case first
    if label == "inconclusive":
        explanation = "O sistema não encontrou um padrão claro de viés neste texto e preferiu não concluir."
        dominant_archetype = "indefinido"
        return explanation, dominant_archetype

    # 2. Identify the dominant archetype for conclusive results
    dominant_index = np.argmax(delta12)
    dominant_archetype = ARCHETYPE_NAMES[dominant_index]

    # 3. Build explanation based on the label
    if label == "neutral":
        explanation = f"O texto não apresenta sinais fortes de viés. Arquétipo dominante: {dominant_archetype}."

    elif label == "biased" and bias_score is not None:
        explanation = (
            f"O texto apresenta sinais de viés (bias_score ≈ {bias_score:.2f}). "
            f"Arquétipo dominante: {dominant_archetype}."
        )
    else:
        # Fallback for unexpected cases
        explanation = "Explicação não disponível."

    return explanation, dominant_archetype
