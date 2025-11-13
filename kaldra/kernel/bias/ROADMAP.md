# ✅ **KALDRA-Bias Roadmap — v0.3 Atualizado**

This roadmap documents the development status and planned evolution of the **KALDRA-Bias** module.

---

# **Phase 1 — Local MVP (v0.3)**

**Objective:** Deliver a functional, uncertainty-aware, explainable bias detection kernel with a stable API, running locally.

### ✔️ Completed

* **Repository scaffolding** (`api/`, `src/`, `data/`, `eval/`, `tests/`)
* **Core documentation** (`README.md`, `MODEL_CARD.md`, `ROADMAP.md`)
* **FastAPI endpoint `/bias/detect`**
* **Embedding generation** (`embeddings.py`)
* **Δ12 projection** (`delta12.py`)
* **Cultural modulation structure (3×48)** with locale mapping (`kindra_3x48.py`)
* **τ-layer (uncertainty policy)** (`tau.py`)
* **Bias scoring v0.1 + Logistic Regression v0.2 compatibility** (`scorer.py`)
* **Δ144 symbolic lookup implementation** (`delta144_mapping.py`)
* **Three-layer explainability** (human, technical, symbolic) (`explain.py`)
* **Signals block (intensity, polarization, emotion_hint)** (`pipeline.py`)
* **risk_level computation**
* **Integration of all components via the main pipeline**
* **Creation of small labeled dataset (`gold.csv`)**
* **Evaluation script (`eval_kaldra_bias.py`)**
* **Basic predictions output file (`preds.csv`)**

### ⚠️ Still Missing / Pending From Phase 1

* **Unit tests** (for Δ12, τ-layer, scoring, API)
* **Integration tests** (end-to-end)
* **Local packaging / Dockerization**

---

# **Phase 2 — Dataset Expansion & Model Quality (v0.4)**

**Objective:** Improve robustness, accuracy, fairness, and model reliability.

### To Do

* **Expand training dataset** significantly (multi-language, multi-domain, multi-demographic)
* Define proper **annotation guidelines** for human raters
* Add **group fairness metrics**, including:

  * demographic parity
  * equalized odds
  * false positive/negative rate gaps
* Add **stratified evaluation reports** inside `eval/metrics.md`
* Improve model calibration (Platt scaling or isotonic regression)
* Transition from LR → **more expressive supervised models** (if dataset grows)
* Add **cross-validation** and hyperparameter search
* Implement **continuous evaluation** with versioning of:

  * datasets
  * models
  * metrics

### Optional (stretch goals)

* Automatic misclassification analysis
* Partial fine-tuning of embeddings model (sentence-transformers)

---

# **Phase 3 — Cultural Calibration (3×48) (v0.5)**

**Objective:** Transform the 3×48 cultural layer from a placeholder into a calibrated, meaningful dimension.

### To Do

* Populate full 3×48 Kindra vectors with:

  * cultural weights
  * cross-cultural adjustments
  * domain-specific signatures
* Evaluate impact of cultural modulation on:

  * bias detection accuracy
  * group fairness
  * overfitting to certain cultures
* Introduce locale-informed default thresholds (τ-layer and risk_level)
* Add calibration tooling inside `scripts/` or `eval/`

---

# **Phase 4 — Symbolic Layer Expansion (v0.6)**

**Objective:** Strengthen symbolic interpretability (Δ144 + hero journey + archetype semantics).

### To Do

* Complete all **144 entries** of Δ144 grid
* Add deeper descriptive fields:

  * narrative tone
  * emotional axis
  * symbolic polarity
  * shadow/secondary archetype relations
* Integrate Δ144 attributes into:

  * explanation_layers.symbolic
  * signals
  * risk_level adjustments (optionally)
* Add small LLM-powered post-processor for symbolic wording (optional)

---

# **Phase 5 — Rigorous Explainability & Safety (v0.7)**

**Objective:** Make KALDRA-Bias explainability production-grade and auditable.

### To Do

* Add **feature attribution** (SHAP/LIME on Δ12 or embedding-level)
* Add uncertainty visualizations (confidence curves)
* Add narrative shift detection:

  * compare Δ12/Δ144 patterns across time windows
* Add tamper-resistant logging (hash-based)
* Document known failure modes and uncertainty boundaries

---

# **Phase 6 — Integration with KALDRA Ecosystem (v0.8)**

**Objective:** Make KALDRA-Bias a fully pluggable module across the KALDRA stack.

### To Do

* Define inter-module data contracts with:

  * **KALDRA-Cultural-Shift**
  * **KALDRA-CrisisMap**
  * **KALDRA-StoryGuard**
* Create shared JSON schema structures (`/schemas/`)
* Build an internal messaging contract (local or via cloud functions)
* Enable KALDRA-Bias to:

  * feed KALDRA-Cultural-Shift (trend tracking)
  * provide signals to CrisisMap
  * act as a firewall layer for StoryGuard

---

# **Phase 7 — Productionization (v1.0+)**

### To Do

* Docker-based local deployment
* Optional Kubernetes deployment
* Logging + Monitoring + Metrics dashboards
* Model registry & versioning
* Canary testing for model updates
* Multi-language production evaluation (pt-BR, en, es)
* API rate limiting and auth (JWT or key-based)
* Scaling strategy (autoscaling, workers, or lightweight edge inference)

---

# Summary

KALDRA-Bias has progressed far beyond the original v0.1 MVP:

* It is now **explainable**, **symbolic**, **uncertainty-aware**, and **modular**.
* v0.3 is a **true kernel**, not a toy prototype.
* The next phases require:

  * more data,
  * calibration,
  * fairness evaluation,
  * symbolic expansion,
  * and integration with the rest of the KALDRA ecosystem.
