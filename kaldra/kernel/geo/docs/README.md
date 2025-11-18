# KALDRA-GEO — Kernel Geopolítico

O **KALDRA-GEO** é o núcleo de análise geopolítica e civilizacional do ecossistema KALDRA.
Ele utilizará o Kernel Universal v0.6 (Δ12 dinâmico, Δ144 não-linear, 3×48 com drift,
Tracy–Widom, Painlevé II, κₚ e máquina 3–6–9) para interpretar discursos, comunicados
oficiais, relatórios estratégicos e metanarrativas globais.

Este README descreve apenas a **estrutura inicial**. A lógica será implementada em steps
posteriores.

## Estrutura Atual

```text
kaldra/kernel/geo/
├── api/
├── data/
├── src/
│   ├── delta12_dynamic.py
│   ├── delta144_dynamic.py
│   ├── kindra_geo_drift.py
│   ├── painleve.py
│   ├── tracy_widom.py
│   ├── kappa_geo.py
│   ├── geo_state_machine.py
│   ├── scorer.py
│   └── pipeline.py
├── tests/
└── docs/
    ├── geo_spec.md
    ├── MODEL_CARD.md
    ├── ROADMAP.md
    └── README.md
```
