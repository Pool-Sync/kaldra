# KALDRA-GEO — Geopolitical Narrative Radar (v0.6)

KALDRA-GEO é o kernel geopolítico do ecossistema KALDRA, baseado no Kernel Universal v0.6.  
Ele utiliza:
- Δ12 dinâmico  
- Δ144 não-linear  
- Kindra 3×48 com drift  
- Tracy–Widom  
- Painlevé II  
- κₚ (curvatura cultural)  
- Gauge-fields culturais  
- Máquina de estados 3–6–9  

O módulo interpreta:
- discursos políticos  
- comunicados oficiais  
- publicações de think tanks  
- relatórios de defesa  
- metanarrativas  
- shifts civilizacionais  
- sinais de risco transnarrativo  

A estrutura abaixo define o núcleo geopolítico que os módulos superiores (Alpha, Product, Bias) poderão consultar.

---

## Estrutura

```
kaldra/kernel/geo/
 ├── api/
 ├── data/
 ├── src/
 │    ├── delta12_dynamic.py
 │    ├── delta144_dynamic.py
 │    ├── kindra_geo_drift.py
 │    ├── painleve.py
 │    ├── tracy_widom.py
 │    ├── kappa_geo.py
 │    ├── geo_state_machine.py
 │    ├── scorer.py
 │    ├── pipeline.py
 ├── tests/
 └── docs/
      ├── geo_spec.md
      ├── MODEL_CARD.md
      └── ROADMAP.md
```

---
