import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

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
    Accepts a text payload and returns a mocked bias detection response.

    In this MVP version, the actual detection logic is not implemented.
    The endpoint returns a fixed, placeholder JSON object.
    """
    # Mocked response for the MVP
    return OutputPayload(
        bias_score=0.1,
        label="neutral",
        confidence=0.5,
        dominant_archetype="Inocente",
        plan=3,
        explanation="Placeholder response. The detection logic is not yet implemented."
    )

# --- Main execution block ---

if __name__ == "__main__":
    """
    Allows the application to be run directly using `python main.py`.
    Useful for local development and testing.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)
