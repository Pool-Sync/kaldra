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
    version="0.2.0", # Version updated to reflect new output structure
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
    Accepts a text payload and returns the result from the analysis pipeline,
    formatted according to the v0.2 output structure.
    """
    analysis_result = analyze_text(payload.text)

    # --- Map Pipeline Output to API Output ---
    # Create placeholder data for the new fields not yet in the pipeline
    placeholder_signals = Signals(
        intensity=analysis_result.get("intensity", 0.0),
        polarization=analysis_result.get("polarization", 0.0),
        emotion_hint=analysis_result.get("emotion_hint", "N/A"),
        attack_target=analysis_result.get("attack_target", "N/A")
    )

    placeholder_explanations = ExplanationLayers(
        human=analysis_result.get("explanation", "Placeholder explanation."),
        technical="Technical explanation not yet implemented.",
        symbolic="Symbolic explanation not yet implemented."
    )

    return OutputPayload(
        bias_score=analysis_result["bias_score"],
        label=analysis_result["label"],
        confidence=analysis_result["confidence"],
        risk_level=analysis_result.get("risk_level", "low"), # Placeholder
        dominant_archetype=analysis_result["dominant_archetype"],
        plan=analysis_result["plan"],
        archetype_detail=analysis_result["archetype_detail"],
        explanation_layers=placeholder_explanations,
        signals=placeholder_signals
    )

# --- Main execution block ---

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
