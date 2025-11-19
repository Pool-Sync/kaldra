import pytest
import sys
from pathlib import Path

# Add the project root's parent directory to the Python path.
PROJECT_ROOT_PARENT = Path(__file__).resolve().parents[4]
sys.path.append(str(PROJECT_ROOT_PARENT))

from kaldra.kernel.safeguard.src.pipeline import analyze_text, analyze_batch


EXPECTED_KEYS = {
    "bias_score",
    "label",
    "confidence",
    "risk_level",
    "dominant_archetype",
    "plan",
    "archetype_detail",
    "explanation_layers",
    "signals",
}


def assert_result_structure(result, is_batch_item=False):
    """
    Verifica se o resultado segue o contrato da pipeline v0.5.
    """
    assert isinstance(result, dict)

    current_expected = set(EXPECTED_KEYS)
    if is_batch_item and "skipped" not in result:
        current_expected.add("input_index")

    missing = current_expected.difference(result.keys())
    assert not missing, f"Missing keys in result: {missing}"

    if "skipped" in result:
         assert "input_index" in result
         assert "text" in result
         assert "skipped" in result
         assert "reason" in result


def test_analyze_batch_basic():
    texts = [
        "Este é um texto neutro sobre políticas públicas.",
        "Este é um texto com opinião forte e polarizada, atacando um grupo específico.",
    ]
    results = analyze_batch(texts, locale="pt-BR")
    assert isinstance(results, list)
    assert len(results) == len(texts)
    for res in results:
        assert_result_structure(res, is_batch_item=True)

def test_plan_is_always_3_6_or_9():
    texts = [
        "Texto neutro de referência.",
        "Texto com conflito político explícito.",
        "Texto emocional sobre identidade e pertencimento.",
    ]
    results = analyze_batch(texts, locale="pt-BR")
    for res in results:
        assert_result_structure(res, is_batch_item=True)
        assert res["plan"] in (3, 6, 9), f"Invalid plan value: {res['plan']}"

def test_analyze_text_empty_is_safe():
    result = analyze_text("", locale="pt-BR")
    assert_result_structure(result) # is_batch_item is False by default
    assert result["bias_score"] == 0.0
    assert result["label"] == "unknown"
    assert result["risk_level"] == "low"
    assert result["confidence"] == 0.0
    assert result["plan"] == 3

def test_analyze_text_very_long_does_not_crash():
    long_text = "Este é um texto muito longo. " * 5000
    result = analyze_text(long_text, locale="pt-BR")
    assert_result_structure(result) # is_batch_item is False by default
    assert result["plan"] in (3, 6, 9)
