# Model Card — KALDRA-Bias v0.5

Este documento descreve o comportamento, arquitetura e limitações da versão **v0.5** do **KALDRA-Bias**, o primeiro kernel operacional do ecossistema KALDRA.

O KALDRA-Bias v0.5 é um sistema de análise textual baseado em:
- Δ12 (projeção arquetípica primária)  
- Painel cultural 3×48 (Kindras)  
- Δ144 (lookup simbólico)  
- τ-layer (uncertainty policy)  
- embeddings determinísticos  
- explicabilidade multilayer  
- API estável  

Este kernel serve como base técnica compartilhada por três verticais:
- **KALDRA-Alpha** (mercado, earnings calls, agentes)  
- **KALDRA-GEO** (geopolítica, narrativas de Estados)  
- **Kindra-for-Product** (UX Drift, análise simbólica de produtos)

---

# 1. Versão Atual — v0.5

A v0.5 entrega:

- Pipeline unificada (`analyze_text` e `analyze_batch`)  
- API completa:
  - `/bias/detect`
  - `/bias/batch_detect`
  - `/health`
- Logging estruturado  
- Embeddings determinísticos (hash-based)  
- Δ12 estável  
- Kindras 3×48 estruturados  
- Δ144 lookup simbólico  
- τ-layer operacional  
- risk_level consistente  
- explainability multilayer  
- Estrutura de diretórios consolidada  
- Testes unitários (incluindo API)  

A v0.5 marca o fechamento da fase **“motor operacional básico”**.

---

# 2. Intended Use

O KALDRA-Bias é projetado para:
- triagem narrativa  
- detecção de vieses linguísticos  
- explicações simbólicas  
- análise estrutural de linguagem  
- suporte a alto nível para moderação e pesquisa  

Também é o “núcleo semântico” para outras verticais do ecossistema KALDRA.

## Não recomendado para
- decisões automatizadas sem revisão humana  
- avaliações morais literais  
- julgamentos éticos diretos  
- uso jurídico sem supervisão  
- interpretação literal dos símbolos Δ144  

O modelo retorna **indicadores simbólicos**, não julgamentos normativos.

---

# 3. Dados e Arquivos de Arquétipos

O KALDRA-Bias v0.5 utiliza quatro arquivos principais:

- `delta12_archetypes.json` – estrutura primária Δ12  
- `delta144_grid.json` – matriz 12×12 (lookup simbólico)  
- `cultural_3x48.json` – 144 Kindras culturais  
- `locales_map.json` – modulação por idioma/região  

Esses arquivos dão a **base simbólica estável**, mas ainda não possuem dinâmica interna.

---

# 4. Arquitetura do Kernel v0.5

A pipeline segue este fluxo:

## 4.1 Embeddings
Backend determinístico, hash-based.  
Zero dependência de rede.  
Reprodutível.  

## 4.2 Δ12 Projection
Projeção em 12 eixos arquetípicos.  

## 4.3 Seleção ∆12 → Kindra 3×48
Lookup estrutural estável (sem drift).

## 4.4 τ-Layer (Uncertainty)
Indica confiança e pode retornar "inconclusive".

## 4.5 Scoring
Heurístico determinístico (ou supervisionado quando modelo joblib está presente).

## 4.6 Δ144 Enrichment
Lookup simbólico, não matemático.

## 4.7 Explainability
Retorna três camadas:
- **Human**  
- **Technical**  
- **Symbolic**

## 4.8 Signals
- intensidade  
- polaridade  
- emoção  
- alvo (placeholder)  

## 4.9 risk_level
Derivado de score + confiança.

---

# 5. Entradas e Saídas

## Entrada:
```json
{ "text": "..." }
Saída:
bias_score
label
confidence
dominant_archetype
archetype_detail
plan (3/6/9)
explanation_layers
signals
risk_level
6. Avaliação
Rodar testes:
pytest -q
Testes cobrem:
API
pipeline
embeddings
estrutura de saída
7. Limitações da v0.5
A v0.5 ainda não implementa o kernel completo descrito no documento PENSADORES:
❌ Δ12 dinâmico
❌ Δ144 dinâmico
❌ 3×48 com cultural-drift
❌ Painlevé II
❌ Tracy–Widom
❌ κₚ (curvatura cultural)
❌ Transição 3–6–9 real
❌ Gauge-fields culturais
❌ Máquina de estados simbólica
A v0.5 é um motor estável mas ainda não vivo.
8. Roadmap — v0.6 (Kernel Universal)
A partir da v0.6, o KALDRA-Bias vai se integrar ao Kernel Universal, implementando:
Δ12 dinâmico
Δ144 não-linear
TW (Tracy–Widom)
Painlevé II
κₚ
Campos de gauge culturais
Kindras com drift real
Motor 3–6–9 verdadeiro
State Machine arquetípica
Essas capacidades permitirão:
KALDRA-Alpha (mercado)
KALDRA-GEO (geopolítica)
Kindra-for-Product (produto/UX)
9. Licença
MIT License.

---

**Importante:**  
- Não crie novos branches.  
- Apenas aplique no `main`, rode os testes, e finalize o commit.
