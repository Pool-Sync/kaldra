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
    version="0.1.0",
)

# --- Pydantic Models ---

class InputPayload(BaseModel):
    text: str

class OutputPayload(BaseModel):
    bias_score: Optional[float]
    label: str
    confidence: float
    dominant_archetype: str
    plan: int
    explanation: str
    archetype_detail: Dict[str, Any]

# --- API Endpoint ---

@app.post("/bias/detect", response_model=OutputPayload)
def detect_bias(payload: InputPayload):
    """
    Accepts a text payload and returns the result from the analysis pipeline.
    """
    analysis_result = analyze_text(payload.text)

    return OutputPayload(
        bias_score=analysis_result["bias_score"],
        label=analysis_result["label"],
        confidence=analysis_result["confidence"],
        dominant_archetype=analysis_result["dominant_archetype"],
        plan=analysis_result["plan"],
        explanation=analysis_result["explanation"],
        archetype_detail=analysis_result["archetype_detail"]
    )

# --- Main execution block ---

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
