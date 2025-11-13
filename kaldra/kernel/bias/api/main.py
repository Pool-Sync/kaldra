import uvicorn
import sys
from pathlib import Path
from typing import Optional, Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel

# Add the 'src' directory to the Python path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from pipeline import analyze_text

app = FastAPI(
    title="KALDRA-Bias API",
    description="API for detecting bias in text using the KALDRA-Bias model.",
    version="0.3.0", # Version updated to reflect full pipeline integration
)

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
    # Call the analysis pipeline to get the full dictionary of results
    analysis_result = analyze_text(payload.text)

    # The pipeline now returns a dictionary that directly matches the fields
    # needed by the Pydantic models. We can unpack it directly.
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
