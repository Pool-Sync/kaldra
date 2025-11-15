# CHANGELOG.md — KALDRA-Bias

Histórico completo das versões do módulo KALDRA-Bias, incluindo evoluções técnicas, estabilidade do kernel e arquitextura de explicabilidade simbólica.

---

# v0.4 — Kernel Stabilization + API Cohesion + Pipeline Hardening
**(versão atual)**

A v0.4 solidifica a transformação do KALDRA-Bias de um protótipo experimental para um kernel funcional, estável e coerente — com pipeline unificada, API contratual estabilizada, testes mínimos funcionando e documentação revisada.

## Added
- **Pipeline unificada `analyze_text()`** agora é o único ponto de entrada para toda inferência:
  - embeddings reais,
  - Δ12 projection aplicada corretamente,
  - cultural modulation 3×48 acoplada,
  - τ-layer atuando como guardião,
  - heuristic score / supervised score (quando disponível),
  - Δ144 symbolic lookup integrado,
  - signals & risk_level,
  - três camadas de explicação.

- **Estabilização total do endpoint `/bias/detect`**:
  - Saída JSON contratual padronizada.
  - Garantia dos campos mínimos para qualquer cliente do KALDRA.

- **Estrutura de pastas totalmente consolidada** (`api/`, `kernel/bias/src/`, `kernel/bias/tests/`, `data/`, `eval/`).

- **Teste automático básico do pipeline**:
  - `test_pipeline_basic.py` garantindo retorno consistente e schema mínimo.

- **Instalação via `pip install -e .`** funcionando corretamente.
  - `pyproject.toml` ajustado.
  - Pacote reconhecido pelo Python importando via raiz.

- **Documentação totalmente atualizada**:
  - `MODEL_CARD.md` alinhado com v0.4.
  - `README.md` atualizado.
  - `ROADMAP.md` atualizado.
  - Estilo das versões anteriores mantido.

## Improved
- **Maior coerência interna entre módulos**: imports padronizados (`from kernel.bias.src...`).
- **Organização da pipeline**:
  - modules coesos,
  - domínio lógico consistente,
  - eliminação de duplicações.
- **Δ144 mais claro e acessível** para camada simbólica.
- **Explanations** (human / technical / symbolic) refinadas, coerentes e realistas.
- **Signals** revisados para refletir a estrutura final do pipeline.

## Fixed
- Corrigidos todos os problemas de importação (ModuleNotFoundError).
- Corrigido o ambiente virtual e execução do pipeline fora da API.
- Corrigido branch principal da pipeline garantindo consistência com a API.
- Corrigido contrato de saída da API para evitar campos faltando.

## Pending
- Bateria completa de testes (Delta12, tau, scorer, API).
- Dataset amplo e anotações human-in-the-loop.
- Fairness metrics (demographic parity, equalized odds, FNR/FPR gaps).
- Cultural calibration real para os 3×48 Kindras.
- Completar Δ144 definitivo (alguns campos ainda placeholders).
- Logging estruturado e telemetria.
- Batch inference.
- `/bias/health` e `/bias/batch_detect` (entrarão na v0.5).
- Trocar embedding placeholder por modelo real mais robusto (MiniLM, E5, Jina).

---

# v0.3 — Multi-Layer Explainability, τ-Layer, Δ144 Enrichment

## Added
- **τ-layer (uncertainty policy)** com retorno `"inconclusive"`.
- Estimativa de confiança baseada em Δ12 (concentração/entropia).
- **Três camadas de explicação**:
  - human,
  - technical,
  - symbolic.
- **Δ144** (archetype × hero-journey stage) como lookup simbólico.
- **Signals**:
  - intensity,
  - polarization,
  - emotion_hint,
  - attack_target.
- **risk_level** derivado de score × confidence.

## Improved
- Compatibilidade total com Logistic Regression (v0.2).
- Modularização do pipeline e maior coerência interna.

## Pending
- Testes,
- Cultural calibration,
- Dataset expansion,
- Fairness metrics.

---

# v0.2 — Supervised Scoring + Evaluation Framework

## Added
- Scoring supervisionado via Logistic Regression.
- Suporte para `model_v02.joblib`.
- Dataset inicial `gold.csv`.
- Script de avaliação (`eval_kaldra_bias.py`).
- Métricas básicas (accuracy/precision/recall/F1).

## Improved
- Separação do training logic (`train.py`).
- Scoring heurístico + supervisionado funcionando de forma híbrida.

## Pending
- Dataset muito limitado,
- Cultural modulation ainda estática.

---

# v0.1 — Initial MVP

## Added
- FastAPI com `/bias/detect`.
- Embeddings com sentence-transformers.
- Δ12 projection.
- Estrutura de 3×48 Kindras.
- Estrutura inicial de Δ144.
- Pastas iniciais (`api/`, `src/`, `data/`, `eval/`).
- Documentação inicial.

## Pending
- Sem τ-layer,
- Sem Δ144 completo,
- Sem scoring real,
- Sem dataset,
- Sem testes.

---

# Conclusão

A v0.4 consolida o **primeiro kernel totalmente funcional** do KALDRA-Bias, preparando terreno para a v0.5, que focará em:

- batch inference,
- health-check API,
- embeddings reais,
- logging estruturado,
- teste ampliado,
- melhorias no tau-layer,
- refino da integração Δ12/Δ144,
- preparação para cultural-drift.
