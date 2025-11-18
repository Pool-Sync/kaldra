# KALDRA-FOR-PRODUCT — Kernel de Produto & Marca

KALDRA-FOR-PRODUCT interpreta produtos e marcas pela ótica do ecossistema simbólico KALDRA,
utilizando Δ12 dinâmico, Δ144 não-linear, Painlevé II, Tracy–Widom, κₚ e state machine 3–6–9.

Este é apenas o setup inicial. A lógica será implementada nas próximas etapas.

## Estrutura Atual

```text
kaldra/kernel/product/
├── api/
├── data/
├── src/
│   ├── delta12_dynamic.py
│   ├── delta144_dynamic.py
│   ├── kindra_product_drift.py
│   ├── painleve.py
│   ├── tracy_widom.py
│   ├── kappa_product.py
│   ├── product_state_machine.py
│   ├── scorer.py
│   └── pipeline.py
├── tests/
└── docs/
    ├── product_spec.md
    ├── MODEL_CARD.md
    ├── ROADMAP.md
    └── README.md
```
