import json
from pathlib import Path
from typing import Tuple, List

# --- Paths ---

DATA_PATH = Path(__file__).parent.parent / "data" / "archetypes"
LOCALES_MAP_PATH = DATA_PATH / "locales_map.json"
CULTURAL_3X48_PATH = DATA_PATH / "cultural_3x48.json"


def _load_json_data() -> Tuple[dict, dict]:
    """
    Carrega os artefatos de modulação cultural.

    - locales_map.json  → mapeia locale para cultura + plano 3/6/9
    - cultural_3x48.json → pesos/vetores culturais por plano (stub em v0.5)

    Em v0.5 estes pesos ainda são placeholders. A função precisa ser
    robusta caso o arquivo esteja vazio ou parcial.
    """
    with open(LOCALES_MAP_PATH, "r", encoding="utf-8") as f:
        locales_map = json.load(f)

    with open(CULTURAL_3X48_PATH, "r", encoding="utf-8") as f:
        cultural_weights = json.load(f)

    return locales_map, cultural_weights


# Carregamento único em import
_LOCALES_MAP, _CULTURAL_WEIGHTS = _load_json_data()


def _resolve_plan_for_locale(locale: str) -> int:
    """
    Resolve o plano 3/6/9 a partir do locale.

    Se o locale não existir no mapa, cai no fallback "en" e,
    em último caso, no plano 3.
    """
    fallback = {"plan": 3}
    culture_info = _LOCALES_MAP.get(locale) or _LOCALES_MAP.get("en", fallback)
    plan = culture_info.get("plan", 3)
    return int(plan)


def _get_plan_weights(plan: int) -> List[float]:
    """
    Retorna os pesos culturais associados ao plano.

    Em v0.5, `cultural_3x48.json` pode estar vazio ou apenas com chaves
    `plan_3`, `plan_6`, `plan_9` sem conteúdo. Neste caso, retornamos
    uma lista vazia e a modulação é efetivamente neutra (no-op).

    Esta função existe para preparar o terreno para a v0.6, onde os
    pesos terão efeito real sobre o vetor Δ12.
    """
    key = f"plan_{plan}"
    weights = _CULTURAL_WEIGHTS.get(key, [])
    # Garantir tipo list mesmo se vier algo inesperado.
    if not isinstance(weights, list):
        return []
    return weights


def apply_kindra(delta12: List[float], locale: str) -> Tuple[List[float], int]:
    """
    Aplica a camada Kindra (3×48) a um vetor Δ12.

    v0.5 (infra de drift):
    - Resolve o plano cultural (3/6/9) com base no locale.
    - Carrega os pesos correspondentes ao plano, se existirem.
    - Se não houver pesos ou o tamanho não for compatível, retorna
      o vetor original (no-op) + o plano, mantendo estabilidade.

    Args:
        delta12: vetor Δ12 (12 dimensões arquetípicas).
        locale: string de locale (ex.: "pt-BR", "en", "es").

    Returns:
        (delta12_modulado, plan)
    """
    plan = _resolve_plan_for_locale(locale)
    plan_weights = _get_plan_weights(plan)

    # v0.5: modulação neutra. Apenas preparamos a infra.
    # Quando os pesos forem calibrados (v0.6), a lógica de multiplicação
    # entrará aqui, respeitando o tamanho de delta12.
    modulated_delta12 = list(delta12)

    return modulated_delta12, plan
