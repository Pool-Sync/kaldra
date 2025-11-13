# Model Card: KALDRA-Bias v0.3

This document describes the current state of the **KALDRA-Bias** model (version 0.3), its behavior, intended use, and limitations.

---

## Version Overview

- **v0.1** – Initial MVP
  - Text → embeddings → Δ12 archetypal projection → simple bias score.
  - Static explanations and no explicit uncertainty handling.

- **v0.2** – Supervised scoring
  - Added a basic supervised component (Logistic Regression) on top of the archetypal representation when a trained model is available.
  - Introduced an evaluation script using a small labeled dataset (`gold.csv`).

- **v0.3** – Multi-layer explainability and symbolic enrichment (current)
  - Introduced a **τ-layer** (tau policy) to explicitly return `inconclusive` when the model’s confidence is low.
  - Added **multi-layer explanations**: human, technical, and symbolic.
  - Integrated **Δ144** as a symbolic lookup (Jung × Hero’s Journey) to enrich archetypal interpretation.
  - Added **signals** (intensity, polarization, emotion hint) and a derived **risk_level**.

---

## Model Overview

The KALDRA-Bias v0.3 model is a pipeline designed to analyze text for potential bias while also providing structured interpretability.

The main steps are:

1. **Embeddings**
   - The input text is converted into a high-dimensional vector using a pre-trained `sentence-transformers` model (`all-MiniLM-L6-v2`).
   - This step is responsible for capturing semantic information.

2. **Archetypal Projection (Δ12)**
   - The embedding is projected into a **12-dimensional archetypal space**, where each dimension corresponds to one of 12 Jungian archetypes.
   - In v0.3, this projection is implemented via a simple block-aggregation + softmax procedure, serving as a pragmatic approximation.

3. **Cultural Modulation (3×48) – Structural Stub**
   - A cultural layer (`3×48` Kindras) is conceptually available and structurally represented via JSON tables.
   - In the current MVP, this modulation is either a no-op or a minimal adjustment, pending richer cultural weights and calibration.

4. **τ-Layer (Uncertainty Handling)**
   - The **τ-layer** computes a confidence score from the Δ12 distribution (e.g., how concentrated the distribution is).
   - If confidence is below a threshold, the system returns `label = "inconclusive"` instead of forcing a biased/neutral decision.
   - This makes the model behave more honestly in ambiguous cases.

5. **Scoring (Bias Score + Label)**
   - When the τ-layer allows a decision:
     - v0.2/v0.3 can use either:
       - A simple heuristic rule on top of Δ12; or
       - A **Logistic Regression** model trained on a small labeled dataset, if `model_v02.joblib` is present.
   - The output includes:
     - `bias_score` (probability-like value)
     - `label` ∈ {`biased`, `neutral`, `inconclusive`}

6. **Δ144 Symbolic Enrichment**
   - A **Δ144 grid** (12 archetypes × 12 hero-journey stages) is used as a **lookup table**.
   - Given the dominant archetype, the system retrieves a corresponding Δ144 cell (when available) with fields like:
     - `jung`
     - `hero_stage`
     - `description`
   - This is used to enrich the symbolic layer of the explanation, not to drive the numeric decision.

7. **Multi-layer Explainability**
   - v0.3 returns explanations in three layers:

     - **Human layer** – simple and direct language for non-technical users.
     - **Technical layer** – includes `bias_score`, confidence, thresholds, and the τ-layer decision.
     - **Symbolic layer** – describes the dominant archetype, journey stage, and plan (3/6/9) as a narrative frame.

8. **Signals and Risk Level**
   - The model also outputs:
     - `signals.intensity` – roughly aligned with `bias_score`.
     - `signals.polarization` – combination of bias_score and confidence.
     - `signals.emotion_hint` – coarse hint such as `"raiva"`, `"tensão"`, `"neutro"`, based on score and label.
     - `signals.attack_target` – placeholder (currently `"indefinido"`).
   - A derived `risk_level` ∈ {`baixo`, `medio`, `alto`, `indefinido`} is computed from `label`, `bias_score`, and confidence.

---

## Intended Use

### Recommended Uses

- **Auditing AI-Generated Content**
  - Analyze LLM outputs to identify potentially biased or skewed language.
  - Provide multi-layer explanations to engineers, policy teams, and stakeholders.

- **Reputational Risk Monitoring**
  - Monitor public communications, marketing copy, or internal documents for narrative patterns associated with risk.
  - Use `risk_level` and `signals` as an early-warning layer (not as a final decision-maker).

- **Content Moderation Support**
  - Assist human moderators by flagging content for review based on bias-related signals.
  - Combine `label`, `bias_score`, and `explanation_layers.human` for triage.

- **Research and Prototyping**
  - Explore how “bias” appears when framed through archetypal and symbolic structures (Δ12 and Δ144).
  - Use as a sandbox to test multi-layer explainability and uncertainty-aware decisions.

### Not Recommended Uses

- **Fully Automated Decisions in Sensitive Contexts**
  - Hiring, credit scoring, insurance, criminal justice, or any domain where decisions materially affect people’s lives.
  - The model should not be a standalone gatekeeper.

- **Moral or Ethical Arbitration**
  - The model reflects patterns from data and hand-designed heuristics, not universal moral truth.
  - It must not be used as an “ethical authority”.

- **Replacement for Human Oversight**
  - KALDRA-Bias is a tool to **augment** human judgment, not to replace it.
  - Output should be interpreted critically, ideally combined with human review and domain expertise.

---

## API Specification (v0.3)

### Endpoint: `/bias/detect`

- **Method**: `POST`
- **Description**: Analyzes a given text for bias and returns scores, risk indicators, and multi-layer explanations.

### Expected Input Format

```json
{
  "text": "The text string to be analyzed."
}
```
### Expected Output Format (v0.3)
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
    "technical": "O modelo estimou bias_score ≈ 0.72 com confiança ≈ 0.68, acima do limiar de 0.5 para viés. O τ-layer não bloqueou a decisão.",
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
### Special case:
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
#### Current MVP Limitations (v0.3)
- **Small Dataset**: The current labeled dataset (gold.csv) is small and limited in diversity. Any performance metrics must be treated as exploratory, not production-grade.
- **Heuristic and Prototype-Level Scoring**: While a Logistic Regression model can be used, the overall scoring logic is still prototype-level. Thresholds and mappings from scores to labels/risk levels are simple heuristics.
- **Static and Coarse-Grained Symbolic Layer**: The Δ144 grid and cultural modulation (3×48) are partially filled and not yet calibrated against real-world cultural data. Symbolic outputs are meaningful as narrative lenses, not as causal explanations.
- **No Rigorous Fairness Audit Yet**: There is no current stratified evaluation by demographic or protected groups. Fairness behavior across subpopulations is unknown and must not be assumed.
- **Language and Domain Coverage**: Although the model can process multiple languages at the embedding level, it has not been systematically evaluated across languages and domains. Explanations and risk levels may be less reliable outside the contexts represented in the initial dataset.

### Future Work (Next Steps for v0.x)
- **Dataset Expansion and Curation**:
  - Build a significantly larger and more diverse labeled dataset.
  - Define clear annotation guidelines for “biased” vs “neutral” to reduce label noise.
  - Include multi-language and multi-domain examples (politics, marketing, everyday speech, etc.).
- **Fairness and Robustness Evaluation**:
  - Design and run evaluations stratified by group (e.g., gender, race, region, language).
  - Measure disparities in error rates and adjust the model or thresholds accordingly.
  - Document known failure modes.
- **Cultural Modulation (3×48) Calibration**:
  - Populate and calibrate the 3×48 cultural layer with real data.
  - Measure whether cultural modulation improves or degrades fairness and accuracy.
- **Improved Scoring Models**:
  - Move beyond simple Logistic Regression when justified by dataset size.
  - Explore calibration methods (e.g., Platt scaling) to make bias_score better aligned with real probabilities.
- **Richer Signal Extraction**:
  - Move from heuristic emotion_hint and attack_target to models that detect:
    - explicit targets (e.g., groups, institutions),
    - sentiment and toxicity,
    - stance (for/against).
  - Integrate these into the signals block in a transparent way.
- **Operationalization and Monitoring**:
  - Add logging, versioning, and monitoring for real deployments.
  - Track drift in distributions of bias_score, labels, and risk_level over time.
