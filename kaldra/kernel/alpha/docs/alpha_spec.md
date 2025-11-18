# SPEC — KALDRA-ALPHA (v0.6)
Documento de especificação inicial do kernel financeiro-narrativo.
Narrative Intelligence for Markets

## 1. Objetivo
Definir o kernel **KALDRA-ALPHA**, especializado em análise narrativa de mercados financeiros, integrando o Kernel Universal v0.6:
- Δ12 dinâmico  
- Δ144 não-linear  
- Painel 3×48 vivo  
- Tracy–Widom  
- Painlevé II  
- κₚ  
- Máquina 3–6–9 real  
- Gauge-fields culturais  

O módulo interpreta:
- earnings calls  
- relatórios financeiros  
- guidance  
- press releases  
- Q&A executiva  
- investor letters  
- metanarrativas corporativas  
- riscos narrativos financeiros  

---

## 2. Entradas

### 2.1 Formato
```json
{
  "text": "...",
  "ticker": "AAPL",
  "quarter": "Q1-2025",
  "metadata": {
    "source": "earnings_call | 10-K | 10-Q | guidance | press_release",
    "language": "en",
    "region": "US"
  }
}
```

---

## 3. Saída

```json
{
  "narrative_score": float,
  "risk_level": "low | medium | high | critical",
  "truth_drift": float,
  "archetype": {
    "delta12": "...",
    "delta144_state": "...",
    "kindra_3x48": "...",
    "state": 3
  },
  "signals": {
    "anomaly_TW": float,
    "painleve_curvature": float,
    "cultural_kappa": float,
    "executive_alignment": float,
    "sentiment_stability": float
  },
  "sections": {
    "prepared_remarks": "...",
    "qa": "...",
    "guidance": "..."
  },
  "explanation_layers": {
    "market": "...",
    "symbolic": "...",
    "technical": "..."
  }
}
```

---

## 4. Módulos Internos

### 4.1 Δ12 Dinâmico
Classificação arquetípica dependente de:
- setor  
- narrativa executiva  
- região  
- época  
- contexto macroeconômico  

### 4.2 Δ144 Não-Linear
Transformação contínua:
```
Δ144' = f(Δ144, κₚ, TW, Painlevé)
```

### 4.3 Painel Cultural 3×48 (drift financeiro)
Modulação por:
- estilo do CEO/CFO  
- cultura corporativa  
- região geoeconômica  
- setor de atuação  

### 4.4 Motor 3–6–9 Real
3 — entropia narrativa  
6 — modulação e filtragem (Painlevé II)  
9 — colapso de verdade narrativa  

### 4.5 Tracy–Widom
Detecção de:
- divergências significativas  
- flutuações incomuns  
- linguagem inflada  
- discrepância entre guidance e métricas  

### 4.6 Painlevé II
- estabilização narrativa  
- dissipação de ruído  
- extração de intenção real  

### 4.7 κₚ — Curvatura Cultural Executiva
Mede dissonância entre:
- narrativa executiva  
- contexto econômico real  
- histórico da empresa  

### 4.8 Executive State Machine
Estados:
- GROWTH  
- CONSERVATION  
- TRANSITION  
- CRISIS  
- REBUILD  

Evolução via 3 → 6 → 9.

---

## 5. Métricas ALPHA

### 5.1 Narrative Score  
Consistência da narrativa financeira.

### 5.2 Truth Drift  
Desvio entre discurso e realidade mensurável.

### 5.3 Executive Alignment  
Coerência entre CEO/CFO/Board.

### 5.4 Sentiment Stability  
Estabilidade emocional do discurso.

### 5.5 Market Narrative Risk  
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
Financial Preprocessing
   ↓
Embeddings Determinísticos
   ↓
Δ12 Dinâmico
   ↓
Kindra Drift
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
Output ALPHA
```

---

## 7. Estrutura de Diretórios

```
kaldra/kernel/alpha/
 ├── api/
 ├── data/
 ├── src/
 │    ├── delta12_dynamic.py
 │    ├── delta144_dynamic.py
 │    ├── kindra_drift.py
 │    ├── painleve.py
 │    ├── tracy_widom.py
 │    ├── kappa.py
 │    ├── state_machine.py
 │    ├── scorer.py
 │    ├── pipeline.py
 ├── tests/
 └── docs/
      └── alpha_spec.md
```

---

## 8. API

```
POST /alpha/analyze
POST /alpha/batch
GET  /alpha/health
```

---

## 9. Testes

### 9.1 Unit Tests
- Δ12 dinâmico  
- Δ144 dinâmico  
- κₚ  
- Painlevé  
- TW  
- Drift financeiro  
- state machine  
- pipeline completo  

### 9.2 Casos Financeiros
- divergência guidance vs histórico  
- contradições CEO/CFO  
- mudança abrupta de postura  
- earnings calls de crise  
- investor letters de transição  

---

## 10. Licença
MIT License.
````
