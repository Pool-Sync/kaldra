import uvicorn
import sys
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

# Add the 'src' directory to the Python path to allow for absolute imports
# This makes the API runnable from the 'api' directory as well.
sys.path.append(str(Path(__file__).parent.parent / "src"))

# Now we can import from the 'src' package
from pipeline import analyze_text


# Create the FastAPI application instance
app = FastAPI(
    title="KALDRA-Bias API",
    description="API for detecting bias in text using the KALDRA-Bias model.",
    version="0.1.0",
)

# --- Pydantic Models for Input and Output ---

class InputPayload(BaseModel):
    """Defines the expected input format."""
    text: str

class OutputPayload(BaseModel):
    """Defines the structure of the JSON response."""
    bias_score: float
    label: str
    confidence: float
    dominant_archetype: str
    plan: int
    explanation: str

# --- API Endpoint ---

@app.post("/bias/detect", response_model=OutputPayload)
def detect_bias(payload: InputPayload):
    """
    Accepts a text payload and returns the result from the analysis pipeline.
    """
    # Call the analysis pipeline with the input text
    analysis_result = analyze_text(payload.text)

    # Populate the output model with the results from the pipeline
    return OutputPayload(
        bias_score=analysis_result["bias_score"],
        label=analysis_result["label"],
        confidence=analysis_result["confidence"],
        dominant_archetype=analysis_result["dominant_archetype"],
        plan=analysis_result["plan"],
        explanation=analysis_result["explanation"]
    )

# --- Main execution block ---

if __name__ == "__main__":
    """
    Allows the application to be run directly using `python main.py`.
    Useful for local development and testing.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
