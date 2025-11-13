# CHANGELOG.md — KALDRA-Bias

## v0.3 — Multi-Layer Explainability, τ-Layer, Δ144 Integration
### Added
- τ-layer (uncertainty policy) with explicit `"inconclusive"` outcome.
- Confidence estimation based on Δ12 concentration.
- Three-layer explainability:
  **human**, **technical**, **symbolic**.
- Δ144 symbolic lookup (archetype × hero-journey stage).
- `signals` block: intensity, polarization, emotion_hint, attack_target.
- `risk_level` computation (baixo/médio/alto/indefinido).
- Expanded API response schema reflecting multi-layer explanation.
- Updated pipeline with Δ144 integration and explanation layers.
- Updated MODEL_CARD, README, and ROADMAP to v0.3 architecture.

### Improved
- Bias scoring now compatible with Logistic Regression (v0.2).
- Explanation quality significantly improved.
- Pipeline modularization and consistency.

### Pending
- Unit tests, integration tests.
- Cultural modulation calibration (3×48).
- Dataset expansion.
- Fairness metrics and stratified evaluation.

---

## v0.2 — Supervised Scoring + Evaluation Framework
### Added
- Logistic Regression scoring option (`model_v02.joblib`).
- Dataset `gold.csv` (initial labeled set).
- `preds.csv` output.
- Evaluation script (`eval_kaldra_bias.py`) with accuracy/precision/recall.
- Basic metrics documentation (`metrics.md`).

### Improved
- Scoring logic: heuristic fallback + supervised path.
- Separation of training logic (`train.py`).

### Pending
- Dataset quality remains low.
- Cultural modulation remains placeholder.

---

## v0.1 — Initial MVP Structure
### Added
- FastAPI endpoint `/bias/detect` returning mock values.
- Embeddings module with sentence-transformers.
- Δ12 projection module.
- Cultural modulation structural files (3×48 + locale map).
- Initial directory structure (`api/`, `src/`, `data/`, `eval/`).
- Baseline documentation (README, MODEL_CARD v0.1, ROADMAP v0.1).

### Pending
- No τ-layer.
- No symbolic layer.
- No real scoring.
- No dataset.
- No evaluation.
