import json
import numpy as np
from pathlib import Path
from typing import Optional, List

# --- Import necessary functions from other modules ---
from .embeddings import get_embedding
from .delta12 import project_to_delta12
from .kindra_3x48 import apply_kindra
from .scorer import compute_bias_score
from .tau import apply_tau_policy
from .explain import build_explanation_layers
from .delta144_mapping import map_to_delta144
from .settings import get_settings, BiasSettings
from .logging_config import get_logger

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

def analyze_text(text: str, locale: str = "pt-BR", settings: Optional[BiasSettings] = None) -> dict:
    """
    Runs the full KALDRA-Bias analysis pipeline on a given text.
    """
    logger = get_logger()
    if settings is None:
        settings = get_settings()

    text_length = len(text or "")
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
        stripped = text.strip()
        if not stripped:
            logger.warning(f"[analyze_batch] Texto vazio na posição {idx}; marcando como skipped.")
            results.append({
                "input_index": idx, "text": text, "skipped": True, "reason": "empty_text",
            })
            continue

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
