import pytest
import sys
from pathlib import Path
from fastapi.testclient import TestClient

# Ensure the repository root is available for namespace imports.
PROJECT_ROOT = Path(__file__).resolve().parents[5]
sys.path.append(str(PROJECT_ROOT))

from kaldra.kernel.bias.api.main import app

EXPECTED_KEYS = {
    "input_index",
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

client = TestClient(app)


def test_healthcheck():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_bias_detect_single():
    payload = {
        "text": "Este é um texto neutro sobre economia.",
        "locale": "pt-BR"
    }

    r = client.post("/bias/detect", json=payload)

    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, dict)
    # For single analysis, input_index is not expected
    missing = EXPECTED_KEYS.difference(data.keys()).difference({"input_index"})
    assert not missing, f"Missing keys: {missing}"

    assert data["plan"] in (3, 6, 9)


def test_bias_detect_empty_text():
    r = client.post("/bias/detect", json={"text": "", "locale": "pt-BR"})

    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, dict)
    # For single analysis, input_index is not expected
    missing = EXPECTED_KEYS.difference(data.keys()).difference({"input_index"})
    assert not missing, f"Missing keys: {missing}"
    assert data["bias_score"] == 0.0
    assert data["label"] == "unknown"
    assert data["risk_level"] == "low"
    assert data["confidence"] == 0.0
    assert data["plan"] == 3


def test_bias_batch_detect():
    payload = {
        "texts": [
            "Texto neutro simples.",
            "Texto com ataque explícito a um grupo."
        ],
        "locale": "pt-BR"
    }

    r = client.post("/bias/batch_detect", json=payload)

    assert r.status_code == 200

    result = r.json()

    assert isinstance(result, list)
    assert len(result) == 2

    for item in result:
        missing = EXPECTED_KEYS.difference(item.keys())
        assert not missing, f"Missing keys: {missing}"
        assert item["plan"] in (3, 6, 9)


def test_bias_detect_long_text():
    long_text = "muito longo " * 5000

    r = client.post("/bias/detect", json={"text": long_text, "locale": "pt-BR"})
    assert r.status_code == 200

    data = r.json()
    # For single analysis, input_index is not expected
    missing = EXPECTED_KEYS.difference(data.keys()).difference({"input_index"})
    assert not missing
    assert data["plan"] in (3, 6, 9)
