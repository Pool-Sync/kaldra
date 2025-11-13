# Model Card: KALDRA-Bias v0.1

This document provides a summary of the KALDRA-Bias model, its characteristics, and its intended use.

## Model Overview

The KALDRA-Bias model is a pipeline designed to analyze text for potential biases. The process follows these steps:
1.  **Embeddings**: The input text is converted into a high-dimensional vector representation using a pre-trained `sentence-transformers` model.
2.  **Archetypal Projection (Δ12)**: The embedding is projected into a 12-dimensional space, where each dimension corresponds to a fundamental archetype.
3.  **Cultural Modulation (3x48)**: A cultural context layer is applied using a table-based mapping to adjust the archetypal weights.
4.  **Scoring**: A simple, pre-trained machine learning model takes the modulated vector as input and calculates a `bias_score`.

---

## Intended Use

### Recommended Uses
-   **Auditing AI-Generated Content**: Analyzing outputs from Large Language Models (LLMs) to identify potentially biased or skewed content.
-   **Reputational Risk Monitoring**: Monitoring public communications, marketing copy, or internal documents for language that could pose a reputational risk.
-   **Content Moderation Support**: Assisting human moderators by flagging content that may require further review.
-   **Research**: Studying how bias is encoded in language through the lens of archetypal frameworks.

### Not Recommended Uses
-   **Sensitive Automated Decisions**: The model should not be used to make fully automated decisions in sensitive areas such as hiring, loan applications, or criminal justice.
-   **Moral or Ethical Judgment**: The model is not a source of absolute truth and should not be treated as a definitive arbiter of morality or ethics.
-   **Replacement for Human Oversight**: KALDRA-Bias is intended to be a tool to augment human judgment, not replace it.

---

## API Specification

### Endpoint: `/bias/detect`

-   **Method**: `POST`
-   **Description**: Analyzes a given text for bias.

#### Expected Input Format
```json
{
  "text": "The text string to be analyzed."
}
```

#### Expected Output Format
```json
{
  "bias_score": 0.82,
  "label": "biased",
  "confidence": 0.91,
  "dominant_archetype": "The Ruler",
  "plan": 6,
  "explanation": "The text exhibits a strong hierarchical worldview, which correlates with biased statements in the training data."
}
```

---

## Limitations and Future Work

### Current MVP Limitations
-   The initial model is trained on a limited dataset and may not generalize well to all contexts.
-   The definition of "bias" is constrained by the archetypal framework and the labels in the training data.
-   The explanations provided are template-based and may lack deep contextual understanding.
-   The cultural modulation is static and does not adapt to evolving linguistic norms.

### Next Steps
-   Expand the dataset with a wider variety of sources and more nuanced examples of bias.
-   Improve the scoring model by exploring more complex architectures and training regimes.
-   Develop a more sophisticated explainability module.
-   Conduct rigorous fairness and performance audits.
