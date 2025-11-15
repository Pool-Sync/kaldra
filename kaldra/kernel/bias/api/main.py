import uvicorn
import sys
from pathlib import Path
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Add the 'src' directory to the Python path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from pipeline import analyze_text
from logging_config import get_logger

app = FastAPI(
    title="KALDRA-Bias API",
    description="API for detecting bias in text using the KALDRA-Bias model.",
    version="0.3.0",
)

logger = get_logger()

# --- Pydantic Models ---

class InputPayload(BaseModel):
    text: str

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
    bias_score: Optional[float]
    label: str
    confidence: float
    risk_level: str
    dominant_archetype: str
    plan: int
    archetype_detail: Dict[str, Any]
    explanation_layers: ExplanationLayers
    signals: Signals

# --- API Endpoint ---

@app.post("/bias/detect", response_model=OutputPayload)
def detect_bias(payload: InputPayload):
    """
    Accepts a text payload and returns the full, structured result from the
    analysis pipeline.
    """
    text_preview = payload.text[:120] if payload.text else ""
    logger.info(
        "KALDRA-Bias /bias/detect called",
        extra={
            "text_preview": text_preview,
        },
    )

    try:
        analysis_result = analyze_text(payload.text)
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

    return OutputPayload(
        bias_score=analysis_result["bias_score"],
        label=analysis_result["label"],
        confidence=analysis_result["confidence"],
        risk_level=analysis_result["risk_level"],
        dominant_archetype=analysis_result["dominant_archetype"],
        plan=analysis_result["plan"],
        archetype_detail=analysis_result["archetype_detail"],
        explanation_layers=analysis_result["explanation_layers"],
        signals=analysis_result["signals"]
    )

# --- Main execution block ---

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
