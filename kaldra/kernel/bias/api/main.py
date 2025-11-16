import uvicorn
from typing import Optional, Dict, Any, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from kernel.bias.src.pipeline import analyze_text, analyze_batch
from kernel.bias.src.logging_config import get_logger

app = FastAPI(
    title="KALDRA-Bias API",
    description="API for detecting bias in text using the KALDRA-Bias model.",
    version="0.5.0",
)

logger = get_logger()

# --- Pydantic Models ---

class InputPayload(BaseModel):
    text: str
    locale: str = "pt-BR"

class BatchInputPayload(BaseModel):
    texts: List[str]
    locale: str = "pt-BR"

class ExplanationLayers(BaseModel):
    human: str
    technical: str
    symbolic: str

class Signals(BaseModel):
    intensity: float
    polarization: float
    emotion_hint: str
    attack_target: str

class OutputPayload(BaseModel):
    input_index: Optional[int] = None
    bias_score: Optional[float]
    label: str
    confidence: float
    risk_level: str
    dominant_archetype: str
    plan: int
    archetype_detail: Dict[str, Any]
    explanation_layers: ExplanationLayers
    signals: Signals

# --- API Endpoints ---

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

@app.post("/bias/detect", response_model=OutputPayload)
def detect_bias(payload: InputPayload):
    text_preview = payload.text[:120] if payload.text else ""
    logger.info(
        "KALDRA-Bias /bias/detect called",
        extra={"text_preview": text_preview, "locale": payload.locale},
    )

    try:
        analysis_result = analyze_text(payload.text, locale=payload.locale)
    except Exception as exc:
        logger.exception("Error in /bias/detect KALDRA-Bias analysis")
        raise HTTPException(
            status_code=500,
            detail="Internal error while running KALDRA-Bias analysis.",
        ) from exc

    logger.info(
        "KALDRA-Bias /bias/detect completed",
        extra={
            "label": analysis_result.get("label"),
            "risk_level": analysis_result.get("risk_level"),
            "plan": analysis_result.get("plan"),
        },
    )

    return OutputPayload(**analysis_result)

@app.post("/bias/batch_detect", response_model=List[OutputPayload])
def detect_bias_batch(payload: BatchInputPayload):
    logger.info(
        "KALDRA-Bias /bias/batch_detect called",
        extra={"batch_size": len(payload.texts), "locale": payload.locale},
    )

    try:
        results = analyze_batch(payload.texts, locale=payload.locale)
    except Exception as exc:
        logger.exception("Error in /bias/batch_detect KALDRA-Bias analysis")
        raise HTTPException(
            status_code=500,
            detail="Internal error during batch analysis.",
        ) from exc

    logger.info(
        "KALDRA-Bias /bias/batch_detect completed",
        extra={"processed_items": len(results)},
    )

    valid_results = [res for res in results if not res.get("skipped")]

    return [OutputPayload(**res) for res in valid_results]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
