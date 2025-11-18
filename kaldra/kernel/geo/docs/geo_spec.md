# SPEC — KALDRA-GEO (v0.6)

## 1. Objetivo
Definir o kernel KALDRA-GEO para análise geopolítica e civilizacional com o Kernel Universal v0.6.

## 2. Entradas
```json
{
  "text": "...",
  "source_type": "speech | official_communique | think_tank | defense_report | geopolitical_analysis",
  "region": "US | EU | CN | RU | LATAM | MENA | AFRICA | GLOBAL",
  "language": "en",
  "metadata": {
    "speaker": "...",
    "institution": "...",
    "date": "YYYY-MM-DD"
  }
}
```

## 3. Saída
Inclui:
- geo_score  
- risk_level  
- narrative vectors  
- Δ12 dinâmico  
- Δ144 estado  
- Kindra 3×48 com drift  
- sinais TW  
- curvatura cultural κₚ  
- state-machine geopolítica  

---
