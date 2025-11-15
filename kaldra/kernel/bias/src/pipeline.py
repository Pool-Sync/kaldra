import json
import numpy as np
from pathlib import Path
from typing import Optional, List

# --- Import necessary functions from other modules ---
from kernel.bias.src.embeddings import get_embedding
from kernel.bias.src.delta12 import project_to_delta12
from kernel.bias.src.kindra_3x48 import apply_kindra
from kernel.bias.src.scorer import compute_bias_score
from kernel.bias.src.tau import apply_tau_policy
from kernel.bias.src.explain import build_explanation_layers
from kernel.bias.src.delta144_mapping import map_to_delta144
from kernel.bias.src.settings import get_settings, BiasSettings
from kernel.bias.src.logging_config import get_logger

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
    if label == "inconclusive" or label == "unknown" or bias_score is None:
        return "indefinido" if label == "inconclusive" else "low"

    score = bias_score * confidence
    if score < 0.3:
        return "baixo"
    elif 0.3 <= score < 0.6:
        return "medio"
    else:
        return "alto"

# --- Main Analysis Pipeline ---

def analyze_text(text: str, locale: str = "pt-BR", settings: Optional[BiasSettings] = None) -> dict:
    """
    Runs the full KALDRA-Bias analysis pipeline on a given text.
    """
    logger = get_logger()
    if settings is None:
        settings = get_settings()

    # Handle empty text case
    if not text or not text.strip():
        logger.warning("analyze_text called with empty or whitespace-only text.")
        return {
            "bias_score": 0.0,
            "label": "unknown",
            "confidence": 0.0,
            "risk_level": "low",
            "dominant_archetype": "indefinido",
            "plan": 3,
            "archetype_detail": {},
            "explanation_layers": {
                "human": "Texto vazio ou inválido.",
                "technical": "Entrada vazia, retornando resultado seguro.",
                "symbolic": "Nenhuma análise simbólica aplicável."
            },
            "signals": compute_signals("unknown", 0.0, 0.0),
        }

    text_length = len(text)
    logger.debug(
        "Analyze_text chamado",
        extra={"event": "analyze_text_start", "locale": locale, "text_length": text_length},
    )

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

    logger.info(
        "Analyze_text concluído",
        extra={
            "event": "analyze_text_end", "label": label, "risk_level": risk_level,
            "plan": plan, "dominant_archetype": dominant_archetype_name,
            "confidence": float(confidence),
            "bias_score": float(bias_score) if bias_score is not None else None,
        },
    )

    return {
        "bias_score": bias_score, "label": label, "confidence": confidence,
        "risk_level": risk_level, "dominant_archetype": dominant_archetype_name,
        "plan": plan, "archetype_detail": delta144_info,
        "explanation_layers": explanation_layers, "signals": signals,
    }

def analyze_batch(
    texts: list[str],
    locale: str = "pt-BR",
    settings: Optional[BiasSettings] = None,
) -> list[dict]:
    """
    Executa a análise de viés em lote, reaproveitando analyze_text.
    """
    if settings is None:
        settings = get_settings()

    logger = get_logger()
    results: list[dict] = []
    MAX_LEN_FOR_LOG = 5000

    for idx, text in enumerate(texts):
        # The check for empty/whitespace string is now handled inside analyze_text
        stripped = text

        if len(stripped) > MAX_LEN_FOR_LOG:
            logger.warning(
                f"[analyze_batch] Texto muito longo na posição {idx} (len={len(stripped)}); "
                "processando mesmo assim."
            )

        logger.info(f"[analyze_batch] Analisando item {idx} (len={len(stripped)})")

        result = analyze_text(text=stripped, locale=locale, settings=settings)

        if isinstance(result, dict) and "input_index" not in result:
            result["input_index"] = idx

        results.append(result)

    logger.info(f"[analyze_batch] Concluído. Itens processados: {len(results)}")
    return results
