# Model Card: KALDRA-Bias v0.4

This document describes the current state of the **KALDRA-Bias** model (version 0.4), its behavior, intended use, and limitations.

---

## Version Overview

- **v0.1 – Initial MVP**
  - Text → embeddings → Δ12 archetypal projection → simple bias score.
  - Static explanations and no explicit uncertainty handling.

- **v0.2 – Supervised scoring**
  - Added a basic supervised component (Logistic Regression) on top of the archetypal representation when a trained model is available.
  - Introduced an evaluation script using a small labeled dataset (`gold.csv`).

- **v0.3 – Multi-layer explainability and symbolic enrichment**
  - Introduced a **τ-layer** (tau policy) to explicitly return `inconclusive` when the model’s confidence is low.
  - Added **multi-layer explanations**: human, technical, and symbolic.
  - Integrated **Δ144** as a symbolic lookup (Jung × Hero’s Journey) to enrich archetypal interpretation.
  - Added **signals** (intensity, polarization, emotion hint) and a derived **risk_level`.

- **v0.4 – API stabilization and kernel hardening (current)**
  - Consolidated the **end-to-end pipeline** as the single entry point for bias analysis.
  - Stabilized the **API contract** of `/bias/detect` (fields, types, and semantics).
  - Clarified separation between:
    - implemented components (embeddings, Δ12, τ-layer, basic scoring, symbolic lookup, explanations, signals), and
    - future work (dataset expansion, fairness metrics, cultural calibration).
  - Prepared the codebase to be testable and ready for integration with the broader KALDRA ecosystem.

---

## Model Overview

KALDRA-Bias v0.4 is a **symbolic + statistical pipeline** designed to analyze text for potential bias and provide structured interpretability.

Main steps:

1. **Embeddings**
   - Input text is converted into a high-dimensional vector using a pre-trained `sentence-transformers` model (e.g. `all-MiniLM-L6-v2`).
   - This step captures the semantic content of the text.

2. **Archetypal Projection (Δ12)**
   - The embedding is projected into a **12-dimensional archetypal space**, each dimension corresponding to one Jungian archetype.
   - v0.4 still uses a pragmatic heuristic (block aggregation + softmax) as an approximation, suitable for an MVP kernel.

3. **Cultural Modulation (3×48)**
   - A cultural layer (`3×48` Kindras) is represented structurally (JSON / tables).
   - In v0.4, this modulation is **lightweight / placeholder**: the structure is present, but full calibration of cultural weights is future work.

4. **τ-Layer (Uncertainty Handling)**
   - The **τ-layer** computes a confidence score from the Δ12 distribution (e.g., how concentrated the probability mass is).
   - If confidence is below a predefined threshold, the system returns `label = "inconclusive"` instead of forcing a `biased`/`neutral` decision.
   - This makes the model more honest in ambiguous contexts and enforces **epistemic safety**.

5. **Scoring (Bias Score + Label)**
   - When the τ-layer allows a decision:
     - v0.4 can use either:
       - a simple heuristic rule over Δ12 and signals; or
       - a **Logistic Regression** model trained on a small labeled dataset, when `model_v02.joblib` is available.
   - Output:
     - `bias_score` (probability-like scalar)
     - `label` ∈ {`biased`, `neutral`, `inconclusive`}

6. **Δ144 Symbolic Enrichment**
   - A **Δ144 grid** (12 archetypes × 12 hero-journey stages) is used as a **lookup table**.
   - Given the dominant archetype, the system retrieves a cell with:
     - `jung`
     - `hero_stage`
     - `description`
     - optional `labels` / tags
   - This layer is used to enrich explanations and provide a narrative/symbolic view. It **does not** drive the numeric decision directly.

7. **Signals and Risk Level**
   - The model also outputs:
     - `signals.intensity` – roughly aligned with `bias_score`.
     - `signals.polarization` – combination of score and confidence.
     - `signals.emotion_hint` – coarse labels such as `"raiva"`, `"tensão"`, `"neutro"`, etc.
     - `signals.attack_target` – placeholder for the main target of the attack (currently `"indefinido"`).
   - A derived `risk_level` ∈ {`baixo`, `medio`, `alto`, `indefinido`} is computed from `label`, `bias_score`, and `confidence`.

---

## Intended Use

### Recommended Uses

- **Auditing AI-Generated Content**
  - Analyze LLM outputs to identify potentially biased or skewed language.
  - Provide multi-layer explanations (human / technical / symbolic) to engineers, policy teams, and stakeholders.

- **Reputational Risk Monitoring**
  - Monitor public communications, marketing copy, or internal documents for narrative patterns associated with risk.
  - Use `risk_level` and `signals` as an **early warning layer**, not as the final arbiter.

- **Content Moderation Support**
  - Assist human moderators by flagging content for review based on bias-related signals.
  - Combine `label`, `bias_score`, and `explanation_layers.human` for triage.

- **Research and Prototyping**
  - Explore how “bias” appears when framed through archetypal and symbolic structures (Δ12 and Δ144).
  - Use as a sandbox to test multi-layer explainability and uncertainty-aware decisions.

### Not Recommended Uses

- **Fully Automated Decisions in Sensitive Contexts**
  - Hiring, credit scoring, insurance, criminal justice, or any domain where decisions materially affect people’s lives.
  - The model must not be used as a standalone gatekeeper.

- **Moral or Ethical Arbitration**
  - The model reflects patterns from data and hand-designed heuristics, not universal moral truth.
  - It must not be treated as an “ethical authority”.

- **Replacement for Human Oversight**
  - KALDRA-Bias is a tool to **augment** human judgment, not to replace it.
  - Output should always be interpreted critically and ideally combined with human review.

---

## API Specification (v0.4)

### Endpoint: `/bias/detect`

- **Method**: `POST`
- **Description**: analyzes a given text for bias and returns scores, risk indicators, archetypal information, and multi-layer explanations.

### Expected Input Format

```json
{
  "text": "The text string to be analyzed."
}
```
### Expected Output Format (v0.4)
```json
{
  "bias_score": 0.72,
  "label": "biased",
  "confidence": 0.68,
  "risk_level": "alto",
  "dominant_archetype": "Fora-da-Lei",
  "plan": 6,
  "archetype_detail": {
    "id": "A05",
    "jung": "Fora-da-Lei",
    "hero_stage": "Chamado à Aventura",
    "description": "",
    "labels": []
  },
  "explanation_layers": {
    "human": "O texto apresenta sinais de viés na forma como descreve pessoas ou grupos.",
    "technical": "O modelo estimou bias_score ≈ 0.72 com confiança ≈ 0.68, acima do limiar de viés, e o τ-layer não bloqueou a decisão.",
    "symbolic": "O texto ressoa com o arquétipo Fora-da-Lei na jornada, sob o plano 6, sugerindo ruptura ou desafio à ordem estabelecida."
  },
  "signals": {
    "intensity": 0.72,
    "polarization": 0.49,
    "emotion_hint": "raiva",
    "attack_target": "indefinido"
  }
}
```
### Special case (uncertain / inconclusive):
```json
{
  "bias_score": null,
  "label": "inconclusive",
  "confidence": 0.21,
  "risk_level": "indefinido",
  "dominant_archetype": "indefinido",
  "plan": 6,
  "archetype_detail": { },
  "explanation_layers": {
    "human": "O sistema não encontrou um padrão claro de viés neste texto e preferiu não concluir.",
    "technical": "A confiança calculada ficou abaixo do limiar do τ-layer, portanto nenhuma decisão de viés foi tomada.",
    "symbolic": "Não há ressonância arquetípica forte o suficiente para atribuir um padrão simbólico consistente."
  },
  "signals": {
    "intensity": 0.0,
    "polarization": 0.0,
    "emotion_hint": "indefinido",
    "attack_target": "indefinido"
  }
}
```
### Limitations
#### Current MVP Limitations (v0.4)
- **Small Dataset**: The labeled dataset (gold.csv) is small and not representative of all contexts. Any quantitative performance claims must be treated as exploratory.
- **Prototype-Level Scoring**: Even with Logistic Regression, the overall scoring logic is still prototype-level, not production-grade.
- **Cultural Modulation Not Fully Calibrated**: The 3×48 Kindra layer exists structurally but is not yet fully calibrated with real cultural weights and cross-cultural evaluation.
- **Symbolic Layer is Partially Populated**: The Δ144 grid is still incomplete and may contain placeholders or empty descriptions.

### Future Work
- Expand training data (multi-language, multi-domain, multi-demographic).
- Define and apply annotation guidelines for human raters.
- Add group fairness metrics and stratified reports.
- Improve model calibration (e.g., Platt scaling or isotonic regression).
- Transition from simple models to more expressive supervised architectures as data grows.
- Complete Δ144 grid and refine 3×48 cultural modulation.
- Add more rigorous unit/integration tests and monitoring for real deployments.
