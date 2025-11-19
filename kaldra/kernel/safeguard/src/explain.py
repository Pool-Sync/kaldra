import json
import numpy as np
from pathlib import Path
from typing import List, Optional, Dict, Any

# --- Constants and Data Loading ---
DATA_PATH = Path(__file__).parent.parent / "data" / "archetypes"
ARCHETYPES_PATH = DATA_PATH / "delta12_archetypes.json"

def _load_archetypes():
    """Loads the archetype names from the JSON file."""
    with open(ARCHETYPES_PATH, "r", encoding="utf-8") as f:
        archetypes_data = json.load(f)
    return [item["name"] for item in sorted(archetypes_data, key=lambda x: x["id"])]

ARCHETYPE_NAMES = _load_archetypes()

# --- V1 Explanation Function (Legacy) ---

def build_explanation(
    delta12: List[float],
    label: str,
    bias_score: Optional[float]
) -> tuple[str, str]:
    """
    Builds a simple, human-readable explanation for the analysis result.
    This is the original, single-string explanation generator.
    """
    if label == "inconclusive":
        explanation = "O sistema não encontrou um padrão claro de viés neste texto e preferiu não concluir."
        dominant_archetype = "indefinido"
        return explanation, dominant_archetype

    dominant_index = np.argmax(delta12)
    dominant_archetype = ARCHETYPE_NAMES[dominant_index]

    if label == "neutral":
        explanation = f"O texto não apresenta sinais fortes de viés. Arquétipo dominante: {dominant_archetype}."
    elif label == "biased" and bias_score is not None:
        explanation = f"O texto apresenta sinais de viés (bias_score ≈ {bias_score:.2f}). Arquétipo dominante: {dominant_archetype}."
    else:
        explanation = "Explicação não disponível."

    return explanation, dominant_archetype

# --- V2 Layered Explanation Function ---

def build_explanation_layers(
    delta12: list[float],
    label: str,
    bias_score: Optional[float],
    confidence: float,
    archetype_name: str,
    delta144_info: Dict[str, Any],
    plan: int
) -> Dict[str, str]:
    """
    Builds a multi-layered explanation of the analysis result.
    """
    # --- Human Layer ---
    if label == "inconclusive":
        human_exp = "O sistema preferiu não concluir sobre este texto devido à baixa confiança na análise."
    elif label == "neutral":
        human_exp = "O texto não apresenta sinais fortes de viés."
    else: # biased
        human_exp = "O texto sugere viés na forma como se refere a pessoas ou grupos."

    # --- Technical Layer ---
    tech_exp = f"Confiança da análise: {confidence:.2f}. "
    if label == "inconclusive":
        tech_exp += "A confiança não atingiu o limiar mínimo (τ-layer) para uma conclusão."
    else:
        # bias_score should not be None here, but we check for safety
        score_str = f"{bias_score:.2f}" if bias_score is not None else "N/A"
        tech_exp += f"O modelo estimou um bias_score de ≈ {score_str}, "
        if label == "biased":
            tech_exp += "ultrapassando o limiar de decisão de 0.5."
        else:
            tech_exp += "permanecendo abaixo do limiar de decisão de 0.5."

    # --- Symbolic Layer ---
    hero_stage = delta144_info.get("hero_stage", "etapa desconhecida")
    symbolic_exp = (
        f"O texto ressoa com o arquétipo {archetype_name}, "
        f"na etapa '{hero_stage}' da jornada, "
        f"sob o plano de modulação cultural {plan}. "
        f"Isso sugere um enquadramento simbólico relacionado a {archetype_name.lower()}."
    )

    return {
        "human": human_exp,
        "technical": tech_exp,
        "symbolic": symbolic_exp,
    }
