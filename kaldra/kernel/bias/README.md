# KALDRA-Bias Kernel (v0.3)

## Overview

**KALDRA-Bias** is the bias analysis engine of the broader KALDRA system.
It evaluates textual content — especially AI-generated outputs — for potential bias, narrative distortions, or harmful framing.

KALDRA-Bias v0.3 provides:

- A **full semantic pipeline** (embeddings → Δ12 → cultural modulation → scoring).
- A **τ-layer** (uncertainty handling), allowing the system to return `"inconclusive"` instead of forcing a decision.
- A **symbolic enrichment layer** using Δ144 (archetype × hero-journey stage).
- A **three-layer explanation module**:
  **human**, **technical**, and **symbolic**.
- A **signals block** with additional diagnostic indicators (intensity, polarization, emotion hint).
- A **risk_level** computed heuristically from the score and the τ-layer confidence.

Together, these components make KALDRA-Bias a transparent, interpretable, and uncertainty-aware bias-detection kernel.

---

## Objectives of MVP v0.3

The v0.3 kernel is designed to deliver **functional, explainable bias analysis** suitable for:

- auditing LLMs,
- content moderation support,
- reputational risk monitoring,
- prototyping cultural/archetypal inference.

It exposes a stable REST endpoint (`/bias/detect`) that returns:

- `bias_score` (float or null),
- `label` (`biased`, `neutral`, or `inconclusive`),
- `confidence` (from τ-layer),
- `risk_level`,
- `dominant_archetype` (Δ12),
- `plan` (3/6/9 cultural mapping),
- `archetype_detail` (from Δ144),
- `explanation_layers` (human / technical / symbolic),
- `signals` (intensity / polarization / emotion_hint / attack_target).

The system is intentionally built to **avoid false certainty** and to provide **contextualized interpretation**, not absolute judgments.

---

## Pipeline Overview

1. **Embeddings**
   - Text is encoded using `sentence-transformers` (`all-MiniLM-L6-v2`).

2. **Δ12 Archetypal Projection**
   - Embedding is reduced into a 12-dimensional archetype space.
   - v0.3 uses a block-average + softmax heuristic.

3. **Cultural Modulation (3×48)**
   - Locale-based modulation using JSON tables.
   - v0.3 uses a lightweight placeholder (preparing for full 3×48 calibration).

4. **τ-Layer (Uncertainty Policy)**
   - Computes confidence based on the concentration of Δ12.
   - If below threshold → label = `"inconclusive"`.

5. **Scoring**
   - If τ-layer allows:
     - simple heuristic OR logistic regression (v0.2/v0.3),
     - returns a `bias_score` and a label.

6. **Symbolic Enrichment (Δ144)**
   - Dominant archetype is mapped to a Δ144 cell (archetype × hero stage).
   - Used to enrich explanations, not to drive scoring.

7. **Explainability (Three Layers)**
   - **Human**: Simple, non-technical description of the decision.
   - **Technical**: Scores, thresholds, τ-layer results.
   - **Symbolic**: Archetype, hero stage, plan (3/6/9) interpretation.

8. **Signals & Risk Level**
   - Additional diagnostic cues:
     - intensity,
     - polarization,
     - emotion_hint,
     - attack_target (placeholder),
   - risk_level derived from score × confidence.

---

## Directory Structure

kaldra-bias/
│
├─ api/
│ ├─ main.py # FastAPI endpoint /bias/detect
│ └─ api_spec.md # API documentation
│
├─ data/
│ ├─ archetypes/
│ │ ├─ delta12_archetypes.json
│ │ ├─ delta144_grid.json
│ │ ├─ cultural_3x48.json
│ │ └─ locales_map.json
│ ├─ datasets/
│ │ ├─ gold.csv # labeled dataset (v0.3)
│ │ └─ preds.csv # evaluation output
│ └─ examples/
│ └─ demo_inputs.md
│
├─ src/
│ ├─ embeddings.py
│ ├─ delta12.py
│ ├─ delta144_mapping.py
│ ├─ kindra_3x48.py
│ ├─ scorer.py
│ ├─ tau.py
│ ├─ explain.py
│ ├─ pipeline.py
│ └─ train.py
│
├─ eval/
│ ├─ eval_kaldra_bias.py
│ └─ metrics.md
│
└─ README.md # this file

---

## Current Status (v0.3)

- ✓ Embeddings module stable
- ✓ Δ12 projection implemented
- ✓ Cultural modulation structured (lightweight placeholder)
- ✓ τ-layer implemented
- ✓ Bias scoring (heuristic + optional logistic regression)
- ✓ Δ144 symbolic lookup
- ✓ Three-layer explainability
- ✓ Signals + risk_level
- ✓ Evaluation script (`eval_kaldra_bias.py`)
- ✓ Minimal dataset available (`gold.csv`)

This version is suitable for **research, experimentation, and early-stage integrations**.

It is **not** ready for:
- production deployment in sensitive environments,
- high-stakes decision-making,
- fairness certification.

---

## Next Steps (towards v0.4/v0.5)

1. Expand dataset and annotation guidelines.
2. Add proper multi-language evaluation.
3. Calibrate cultural modulation (3×48) with real data.
4. Improve scoring model (better supervision + calibration).
5. Add group fairness metrics (precision/recall gaps).
6. Improve Δ144 descriptions and hero-stage mapping.
7. Implement monitoring and logging for real deployments.

---

KALDRA-Bias aims to offer a **transparent, explainable, and archetype-aware** perspective on textual bias — with safety through doubt (τ-layer) and clarity through layered explanations.
