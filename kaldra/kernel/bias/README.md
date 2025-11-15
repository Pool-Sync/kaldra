# KALDRA-Bias Kernel (v0.4)

## Overview

**KALDRA-Bias** is the bias analysis engine of the broader KALDRA system.
It evaluates textual content — especially AI-generated outputs — for potential bias, narrative distortions, or harmful framing.

KALDRA-Bias v0.4 provides:

- A **full semantic pipeline** (embeddings → Δ12 → cultural modulation → scoring).
- A **τ-layer** (uncertainty handling), allowing the system to return `"inconclusive"` instead of forcing a decision.
- A **symbolic enrichment layer** using Δ144 (archetype × hero-journey stage).
- A **three-layer explanation module**:
  **human**, **technical**, and **symbolic**.
- A **signals block** with additional diagnostic indicators (intensity, polarization, emotion hint, attack target).
- A **risk_level** computed heuristically from the score and the τ-layer confidence.
- A **stable REST API endpoint** (`/bias/detect`) suitable for local use and for integration with other KALDRA modules.

Together, these components make KALDRA-Bias a transparent, interpretable, and uncertainty-aware bias-detection kernel.

---

## Objectives of MVP v0.4

The v0.4 kernel is designed to deliver **functional, explainable bias analysis** suitable for:

- auditing LLMs,
- content moderation support,
- reputational risk monitoring,
- prototyping cultural/archetypal inference.

The system focuses on three pillars:

1. **Detection** – produce a bias score + label.
2. **Doubt** – explicitly model uncertainty via τ-layer and allow `inconclusive`.
3. **Meaning** – enrich analysis with archetypes (Δ12/Δ144) and narrative signals.

It exposes a REST endpoint (`/bias/detect`) that returns:

- `bias_score` (float or null),
- `label` (`biased`, `neutral`, or `inconclusive`),
- `confidence` (from τ-layer),
- `risk_level`,
- `dominant_archetype` (Δ12),
- `plan` (3/6/9),
- `archetype_detail` (from Δ144),
- `explanation_layers` (human / technical / symbolic),
- `signals` (intensity / polarization / emotion_hint / attack_target).

The system is intentionally built to **avoid false certainty** and to provide **contextualized interpretation**, not absolute judgments.

---

## Pipeline Overview

1. **Embeddings**
   - Text is encoded using a `sentence-transformers` model (e.g. `all-MiniLM-L6-v2`).
   - Produces a dense vector representation.

2. **Δ12 Archetypal Projection**
   - Embedding is reduced into a 12-dimensional archetype space.
   - v0.4 uses a block-average + softmax heuristic as a practical approximation.

3. **Cultural Modulation (3×48)**
   - Locale-based modulation using JSON tables (3 plans × 48 cultural vectors).
   - In v0.4, this is structurally present and used as a **lightweight modulation**; full calibration is future work.

4. **τ-Layer (Uncertainty Policy)**
   - Computes confidence from the Δ12 distribution (e.g., entropy or concentration).
   - If confidence is below a threshold → `label = "inconclusive"` and `bias_score = null`.

5. **Scoring**
   - If the τ-layer allows:
     - a simple heuristic OR
     - a Logistic Regression model (if trained model is available) produces `bias_score` and `label`.

6. **Symbolic Enrichment (Δ144)**
   - Dominant archetype is mapped onto a Δ144 cell (archetype × hero stage).
   - Used only to **enrich explanations**, not as a direct driver for the numeric decision.

7. **Explainability (Three Layers)**
   - **Human**: plain-language explanation of what the system “saw”.
   - **Technical**: scores, thresholds, τ-layer decision, signals.
   - **Symbolic**: archetype, hero stage, plan (3/6/9) and narrative reading.

8. **Signals & Risk Level**
   - Additional diagnostic cues:
     - `intensity`,
     - `polarization`,
     - `emotion_hint`,
     - `attack_target` (currently a placeholder).
   - `risk_level` derived from score × confidence and label.

---

## Directory Structure

_Example structure for the kernel (can be adapted as the repo evolves):_

```text
kaldra-bias/
│
├─ api/
│  ├─ main.py            # FastAPI app exposing /bias/detect
│  └─ api_spec.md        # API documentation and examples
│
├─ data/
│  ├─ archetypes/
│  │  ├─ delta12_archetypes.json
│  │  ├─ delta144_grid.json
│  │  ├─ cultural_3x48.json
│  │  └─ locales_map.json
│  ├─ datasets/
│  │  ├─ gold.csv        # labeled dataset (small, prototype-level)
│  │  └─ preds.csv       # evaluation output (optional)
│  └─ examples/
│     └─ demo_inputs.md
│
├─ src/
│  ├─ embeddings.py
│  ├─ delta12.py
│  ├─ delta144_mapping.py
│  ├─ kindra_3x48.py
│  ├─ scorer.py
│  ├─ tau.py
│  ├─ explain.py
│  ├─ pipeline.py
│  └─ train.py           # optional training / retraining hooks
│
├─ eval/
│  ├─ eval_kaldra_bias.py
│  └─ metrics.md
│
├─ tests/
│  ├─ test_pipeline.py   # unit/integration tests for the pipeline (to grow over time)
│  └─ ...
│
└─ README.md             # this file
```
## Current Status (v0.4)
- ✓ Embeddings module implemented
- ✓ Δ12 projection implemented
- ✓ Cultural modulation structured (lightweight placeholder)
- ✓ τ-layer implemented
- ✓ Bias scoring (heuristic + optional logistic regression)
- ✓ Δ144 symbolic lookup
- ✓ Three-layer explainability
- ✓ Signals + risk_level
- ✓ API endpoint /bias/detect wired to the pipeline
- ⚠️ Still prototype in the following aspects:
  - Dataset size and coverage (gold.csv is small).
  - Fairness metrics and group-level evaluation.
  - Cultural calibration (3×48).
  - Automated tests and CI are minimal and should be expanded.

This version is suitable for **research, experimentation, and early-stage integrations**, not for high-stakes production.

## Next Steps (beyond v0.4)
- Expand dataset and annotation guidelines.
- Add proper multi-language evaluation.
- Calibrate cultural modulation (3×48) with real data.
- Improve scoring model (better supervision + calibration).
- Add group fairness metrics and stratified reports.
- Complete Δ144 descriptions and hero-stage mapping.
- Improve monitoring, logging and CI for real deployments.

KALDRA-Bias aims to offer a **transparent, explainable, archetype-aware** perspective on textual bias — with safety through doubt (τ-layer) and clarity through multi-layer explanations.
