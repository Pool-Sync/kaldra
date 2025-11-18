# SPEC — KALDRA-GEO (v0.6)
Geopolitical Narrative Radar

## 1. Objetivo
Definir o kernel **KALDRA-GEO**, especializado em análise geopolítica, civilizacional e estratégica, utilizando o Kernel Universal v0.6:
- Δ12 dinâmico  
- Δ144 não-linear  
- Painel 3×48 com drift  
- Tracy–Widom  
- Painlevé II  
- κₚ  
- Máquina 3–6–9  
- Campos de gauge culturais  

O módulo interpreta:
- discursos  
- comunicados oficiais  
- relatórios estratégicos  
- think tanks  
- doutrinas  
- metanarrativas  
- riscos transnarrativos  

---

## 2. Entradas

### 2.1 Formato
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

---

## 3. Saída

```json
{
  "geo_score": float,
  "risk_level": "low | moderate | high | critical",
  "archetype": {
    "delta12": "...",
    "delta144_state": "...",
    "kindra_3x48": "...",
    "state": 3
  },
  "narrative_vectors": {
    "power_projection": float,
    "strategic_posture": float,
    "conflict_tension": float,
    "cooperation_level": float,
    "civilizational_drift": float
  },
  "signals": {
    "anomaly_TW": float,
    "painleve_curvature": float,
    "cultural_kappa": float,
    "policy_shift_index": float,
    "alignment_shift": float
  },
  "subsections": {
    "intent": "...",
    "capabilities": "...",
    "strategic_position": "...",
    "metanarrative": "..."
  }
}
```

---

## 4. Módulos Internos

### 4.1 Δ12 Dinâmico
Classificação arquetípica dependente de:
- postura estatal  
- intenção estratégica  
- cultura política  
- alinhamentos internacionais  

### 4.2 Δ144 Não-Linear
Transformação contínua:
```
Δ144' = f(Δ144, κₚ, TW, Painlevé)
```

### 4.3 Painel Cultural 3×48 (drift civilizacional)
Modulação por:
- civilização  
- ideologia  
- bloco geoeconômico  
- doutrina militar  

### 4.4 Motor 3–6–9 Real
3 — entropia do discurso  
6 — modulação simbólica  
9 — colapso narrativo  

### 4.5 Tracy–Widom
Detecção de:
- rupturas  
- declarações extremas  
- mudanças abruptas  

### 4.6 Painlevé II
- filtragem não-linear  
- suavização semântica  
- extração de intenção real  

### 4.7 κₚ — Curvatura Cultural Geopolítica
Mede dissonância entre:
- discurso oficial  
- cultura política  
- interesses reais  

### 4.8 Máquina de Estados Geopolítica
Estados:
- COOPERATION  
- TENSION  
- COMPETITION  
- HOSTILITY  
- CRISIS  
- REORDERING  

Evolução via 3 → 6 → 9.

---

## 5. Métricas GEO

### 5.1 Geo Score  
Consistência estratégica geral.

### 5.2 Civilizational Drift  
Variação narrativa em relação ao bloco civilizacional.

### 5.3 Power Projection Index  
Intensidade da intenção de poder.

### 5.4 Alignment Shift  
Mudanças diplomáticas e estratégicas.

### 5.5 Transnarrative Risk  
Resultado de:
- TW  
- κₚ  
- Δ144 deformado  
- state machine  

---

## 6. Pipeline

```
Raw Text
   ↓
Preprocessing Geopolítico
   ↓
Embeddings Determinísticos
   ↓
Δ12 Dinâmico
   ↓
Kindra Drift 3×48
   ↓
Painlevé II
   ↓
Δ144 Não-Linear
   ↓
Tracy–Widom
   ↓
κₚ
   ↓
State Machine 3–6–9
   ↓
Output GEO
```

---

## 7. Estrutura de Diretórios

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
      └── geo_spec.md
```

---

## 8. API

```
POST /geo/analyze
POST /geo/batch
GET  /geo/health
```

---

## 9. Testes

### 9.1 Unit Tests
- Δ12 dinâmico  
- Δ144 dinâmico  
- κₚ  
- Painlevé  
- TW  
- Drift civilizacional  
- GEO state machine  
- pipeline completo  

### 9.2 Casos Geopolíticos
- discursos de crise  
- comunicados pós-conflito  
- realinhamentos estratégicos  
- análises de think tanks  
- documentos de defesa  

---

## 10. Licença
MIT License.
