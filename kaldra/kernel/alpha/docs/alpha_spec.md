# SPEC KALDRA-ALPHA — Narrative Intelligence for Markets (v0.6)

## 1. Objetivo

Definir o kernel **KALDRA-Alpha** para análise narrativa de mercados financeiros, integrando o **Kernel Universal v0.6** (Δ12 dinâmico, Δ144 não-linear, 3×48 com drift, TW, Painlevé, κₚ e máquina 3–6–9 real) para interpretar:

* earnings calls
* relatórios financeiros
* guidance
* chamadas de resultados
* narrativa executiva
* sinais KALDRA (arquétipo, drift, verdade narrativa, risco)

O SPEC descreve comportamento, entradas, saídas, estrutura, módulos internos e dependências exigidas pelo Codex.

---

## 2. Entradas

### 2.1 Entrada primária

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

### 2.2 Tipos de texto válidos

* prepared remarks
* Q&A
* filings (10-K, 10-Q, 8-K)
* investor letters
* CFO/CEO narrative
* M&A announcements

---

## 3. Outputs do Kernel Alpha

### 3.1 Saída principal

```json
{
  "narrative_score": float,
  "risk_level": "low | medium | high | critical",
  "truth_drift": float,
  "archetype": {
    "delta12": "...",
    "delta144_state": "...",
    "kindra_3x48": "...",
    "state": 3 | 6 | 9
  },
  "signals": {
    "anomaly_TW": float,
    "painleve_curvature": float,
    "cultural_kappa": float,
    "executive_alignment": float,
    "sentiment_stability": float
  },
  "sections": {
    "prepared_remarks": {...},
    "qa": {...},
    "guidance": {...}
  },
  "explanation_layers": {
    "market": "...",
    "symbolic": "...",
    "technical": "..."
  }
}
```

### 3.2 Objetivo do output

Retornar **a verdade narrativa financeira**, detectando:

* dissonância executiva
* promessas infladas
* deriva entre guidance e realidade
* shifts culturais
* rupturas arquetípicas
* anomalias estatísticas

---

## 4. Módulos internos (v0.6)

### 4.1 Δ12 Dinâmico

Cálculo arquetípico dependente de:

* discurso financeiro
* região
* época
* contexto macroeconômico

### 4.2 Δ144 Não-Linear

Transformação contínua:

```
Δ144' = f(Δ144, κₚ, TW, Painlevé)
```

### 4.3 Painel Cultural 3×48 (drift financeiro)

Aplicação do modelo Kindra vivo:

* CFO/CEO tone
* postura cultural da empresa
* região geoeconômica
* setor

### 4.4 Motor 3–6–9 Real

**3** = entropia narrativa do texto
**6** = modulação e filtragem (Painlevé II)
**9** = colapso de verdade narrativa

### 4.5 Tracy–Widom

Detecção de:

* padrões anômalos de discurso
* exageros estatísticos
* divergência entre guidance e facts

### 4.6 Painlevé II

Função:

* suavização não-linear de ruído
* análise de consistência interna do CFO/CEO

### 4.7 κₚ (curvatura cultural executiva)

Mede a **afinidade entre narrativa e contexto econômico real**.

### 4.8 Máquina de Estados Narrativa (Finance State Machine)

Estados:

1. **ASSERTIVE** (crescimento)
2. **DEFENSIVE** (proteção)
3. **TRANSITION** (mudança estrutural)
4. **CRISIS** (linguagem de urgência)
5. **REBUILD** (reconstrução)

Estado inferido pela evolução 3→6→9.

---

## 5. Métricas KALDRA-Alpha

### 5.1 Narrative Score

Avalia consistência entre:

* CFO vs CEO
* guidance vs histórico
* narrativa vs métricas quantitativas

### 5.2 Truth Drift

Desvio entre narrativa e realidade mensurável.

### 5.3 Executive Alignment

Coerência entre partes do discurso.

### 5.4 Sentiment Stability

Estabilidade da emoção segundo Δ144 dinâmico.

### 5.5 Risk Level

Baseado em:

* TW
* κₚ
* transições 3–6–9
* rupturas de arquétipo

---

## 6. Arquitetura do Pipeline Alpha

```
Raw Text
   ↓
Preprocessing Financeiro
   ↓
Embeddings Determinísticos (hash)
   ↓
Δ12 Dinâmico
   ↓
Kindra 3×48 Drift
   ↓
Painlevé II (limpeza semântica)
   ↓
Δ144 Não-Linear
   ↓
Tracy–Widom (anomalias)
   ↓
κₚ (curvatura cultural executiva)
   ↓
State Machine 3–6–9
   ↓
Outputs Financeiros KALDRA-Alpha
```

---

## 7. Requisitos Técnicos para Implementação (Codex)

### 7.1 Estrutura esperada de diretórios

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
 └── alpha_spec.md
```

### 7.2 Dependências internas

* Mesmo backend de embeddings do Bias
* Acesso aos arquivos:

  * delta12_archetypes.json
  * delta144_grid.json
  * cultural_3x48.json
  * locales_map.json

### 7.3 API necessária

```
POST /alpha/analyze
POST /alpha/batch
GET  /alpha/health
```

---

## 8. Critérios de Teste

### 8.1 Unit tests obrigatórios

* Δ12 dinâmico
* Δ144 dinâmico
* Painlevé
* TW
* κₚ
* 3×48 drift
* State machine 3-6-9
* pipeline end-to-end

### 8.2 Testes de consistência financeira

* divergência guidance vs discurso
* coerência CEO/CFO
* detecção de contradições

---

## 9. Licenciamento

MIT (igual ao kernel Bias).

---

**SPEC finalizado.**
