# KALDRA-ALPHA — Kernel Financeiro-Narrativo

KALDRA-ALPHA é o núcleo de interpretação financeira do ecossistema KALDRA.
Baseado no Kernel Universal v0.6, ele aplicará Δ12 dinâmico, Δ144 não-linear,
Painlevé II, Tracy–Widom, κₚ e state machine 3–6–9 para interpretar earnings calls,
guidance, Q&A executiva e relatórios financeiros.

Este README descreve apenas a estrutura inicial.

## Estrutura Atual

```text
kaldra/kernel/alpha/
├── api/
├── data/
├── src/
│   ├── delta12_dynamic.py
│   ├── delta144_dynamic.py
│   ├── kindra_drift.py
│   ├── painleve.py
│   ├── tracy_widom.py
│   ├── kappa.py
│   ├── state_machine.py
│   ├── scorer.py
│   └── pipeline.py
├── tests/
└── docs/
    ├── alpha_spec.md
    ├── MODEL_CARD.md
    ├── ROADMAP.md
    └── README.md
```
