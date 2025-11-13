# KALDRA-Bias API Specification

This document details the API endpoints for the KALDRA-Bias module.

## Endpoint: `/bias/detect`

-   **Method**: `POST`
-   **Description**: Analyzes a given text for potential bias and returns a structured assessment.

### Request

The endpoint expects a JSON object with a single key, `text`.

#### Example Input
```json
{
  "text": "This is the text that will be analyzed for bias."
}
```

### Response

The endpoint returns a JSON object containing the results of the bias analysis.

#### Example Output
```json
{
  "bias_score": 0.1,
  "label": "neutral",
  "confidence": 0.5,
  "dominant_archetype": "Inocente",
  "plan": 3,
  "explanation": "Placeholder response. The detection logic is not yet implemented."
}
```

---
**Note**: The current implementation (v0.1) returns a mocked, static response. The actual bias detection logic will be implemented in a future version.
