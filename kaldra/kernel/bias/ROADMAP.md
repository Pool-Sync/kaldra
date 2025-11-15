# ✅ KALDRA-Bias Roadmap — v0.4 Atualizado

This roadmap documents the development status and planned evolution of the **KALDRA-Bias** module.

---

## Phase 1 — Local MVP Kernel (v0.3 concluída / mantida em v0.4)

**Objective:** Deliver a functional, uncertainty-aware, explainable bias detection kernel with a stable API, running locally.

### ✔️ Completed

- Repository scaffolding (`api/`, `src/`, `data/`, `eval/`, `tests/`).
- Core documentation (`README.md`, `MODEL_CARD.md`, `ROADMAP.md`).
- FastAPI endpoint `/bias/detect`.
- Embedding generation (`embeddings.py`).
- Δ12 projection (`delta12.py`).
- Cultural modulation structure (3×48) with locale mapping (`kindra_3x48.py`).
- τ-layer (uncertainty policy) (`tau.py`).
- Bias scoring v0.1 + Logistic Regression compatibility v0.2 (`scorer.py`).
- Δ144 symbolic lookup implementation (`delta144_mapping.py`).
- Three-layer explainability (human, technical, symbolic) (`explain.py`).
- Signals block (intensity, polarization, emotion_hint, attack_target) (`pipeline.py`).
- `risk_level` computation.
- End-to-end pipeline integration (text → response JSON).
- Basic evaluation script (`eval_kaldra_bias.py`) and prototype dataset (`gold.csv`).

### ⚠️ Still Missing / Pending From Phase 1

- Unit tests (for Δ12, τ-layer, scoring, API).
- Integration tests (end-to-end, from `/bias/detect`).
- Local packaging / Dockerization for easy local deployment.

Phase 1 is **functionally complete** but still lacks **robust testing and packaging**.

---

## Phase 2 — Dataset Expansion & Model Quality (targets v0.5)

**Objective:** Improve robustness, accuracy, fairness, and model reliability.

### To Do

- Expand the training dataset significantly (multi-language, multi-domain, multi-demographic).
- Define proper annotation guidelines for human raters.
- Add **group fairness metrics**, including:
  - demographic parity,
  - equalized odds,
  - false positive/negative rate gaps.
- Add stratified evaluation reports inside `eval/metrics.md`.
- Improve model calibration (Platt scaling, isotonic regression or similar).
- Transition from LR → more expressive supervised models as the dataset grows.
- Add cross-validation and basic hyperparameter search.
- Implement **continuous evaluation** with versioning of:
  - datasets,
  - models,
  - metrics.

### Optional (stretch goals)

- Automatic misclassification analysis.
- Partial fine-tuning of the embeddings model (sentence-transformers).

---

## Phase 3 — Cultural Calibration (3×48) (v0.6)

**Objective:** Transform the 3×48 cultural layer from a placeholder into a calibrated, meaningful dimension.

### To Do

- Populate full 3×48 Kindra vectors with:
  - cultural weights,
  - cross-cultural adjustments,
  - domain-specific signatures.
- Evaluate impact of cultural modulation on:
  - bias detection accuracy,
  - group fairness,
  - overfitting to specific cultures.
- Introduce locale-informed default thresholds (τ-layer and `risk_level`).
- Add calibration tooling inside `scripts/` or `eval/`.

---

## Phase 4 — Symbolic Layer Expansion (Δ144) (v0.7)

**Objective:** Strengthen symbolic interpretability (Δ144 + hero journey + archetype semantics).

### To Do

- Complete all **144 entries** of the Δ144 grid.
- Add deeper descriptive fields:
  - narrative tone,
  - emotional axis,
  - symbolic polarity,
  - shadow/secondary archetype relationships.
- Integrate Δ144 attributes into:
  - `explanation_layers.symbolic`,
  - `signals`,
  - optional `risk_level` adjustments.
- Add a small LLM-powered post-processor for symbolic wording (optional).

---

## Phase 5 — Rigorous Explainability & Safety (v0.8)

**Objective:** Make KALDRA-Bias explainability production-grade and auditable.

### To Do

- Add feature attribution (e.g. SHAP/LIME on Δ12 or embedding-level).
- Add uncertainty visualizations (confidence curves).
- Add narrative shift detection:
  - compare Δ12/Δ144 patterns across time windows.
- Add tamper-resistant logging (e.g. hash-based).
- Document known failure modes and uncertainty boundaries.

---

## Phase 6 — Integration with KALDRA Ecosystem (v0.9)

**Objective:** Make KALDRA-Bias a fully pluggable module across the KALDRA stack.

### To Do

- Define inter-module data contracts with:
  - **KALDRA-Cultural-Shift**,
  - **KALDRA-CrisisMap**,
  - **KALDRA-StoryGuard**.
- Create shared JSON schema structures (`/schemas/`).
- Build an internal messaging contract (local or via cloud functions).
- Enable KALDRA-Bias to:
  - feed KALDRA-Cultural-Shift (trend tracking),
  - provide signals to CrisisMap,
  - act as a firewall layer for StoryGuard.

---

## Phase 7 — Productionization (v1.0+)

### To Do

- Docker-based local deployment.
- Optional Kubernetes deployment.
- Logging + monitoring + metrics dashboards.
- Model registry & versioning.
- Canary testing for model updates.
- Multi-language production evaluation (pt-BR, en, es).
- API rate limiting and auth (JWT or key-based).
- Scaling strategy (autoscaling, workers, or lightweight edge inference).

---

## Version Summary

KALDRA-Bias has evolved from a simple archetypal heuristic (v0.1) into a **symbolic + statistical, uncertainty-aware kernel** (v0.4) with:

- stable API,
- multi-layer explainability,
- basic dataset and evaluation,
- clear roadmap for fairness, culture, and symbolic depth.

The next steps are **data, calibration, and integration**, not more complexity in the core math.
