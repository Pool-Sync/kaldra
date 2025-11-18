# KALDRA (v0.5)

KALDRA é um sistema de interpretação simbólica, cultural e narrativa estruturado para atuar em múltiplas camadas de análise — bias, produtos, narrativas, agentes, geopolítica e cultura.

A versão **v0.5** inaugura a estrutura formal do **KALDRA-Bias**, o primeiro kernel operacional do ecossistema, e prepara a base comum para:
- **KALDRA-Alpha** (agentes / alinhamento narrativo)  
- **KALDRA-GEO** (análise geopolítica e cultural)  
- **Kindra-for-Product** (interpretação simbólica aplicada a marcas e produtos)

Essa base comum é sustentada por três camadas:
1. **Arquétipos Delta12** (padrões primários)  
2. **Matriz 12×12 Delta144** (profundidade simbólica expandida)  
3. **Painel Cultural 3×48 (Kindras)** (variação por cultura / contexto)

E interpretada por um motor narrativo inspirado em quatro pensadores:
- **Nietzsche**  
- **Jung**  
- **Campbell**  
- **Marcus Aurelius**

---

# 🚀 Estrutura do Ecossistema KALDRA

KALDRA é composto por módulos independentes que compartilham:
- estrutura de dados  
- princípios narrativos  
- lógica arquetípica  
- camadas de explicação  
- mapas culturais  

| Módulo | Status | Finalidade |
|--------|--------|-------------|
| **KALDRA-Bias** | ✔️ Ativo | Análise de vieses em linguagem natural, com explicações simbólicas. |
| **KALDRA-Alpha** | 🔜 Planejado | Núcleo de alinhamento, narrativa de agentes e intencionalidade. |
| **KALDRA-GEO** | 🔜 Planejado | Radar geopolítico, variações culturais e leitura civilizatória. |
| **Kindra-for-Product** | 🔜 Planejado | Tradução arquetípica e cultural para produtos, UX e branding. |

A v0.5 implementa integralmente o **KALDRA-Bias**, mas a arquitetura já é pensada para expansão.

---

# 🧠 Motor “Pensadores” (v0.5)

O motor narrativo do KALDRA combina:
- **Nietzsche** → Vontade, potência, inversões narrativas  
- **Jung** → Arquétipos, sombra, anima/animus  
- **Campbell** → Estrutura da Jornada do Herói  
- **Marcus Aurelius** → Disciplina, perspectiva e ética  

Cada resultado do kernel Bias produz:
- `dominant_archetype` (delta12 ou delta144)  
- `plan` (3, 6 ou 9)  
- `archetype_detail`  
- `bias_score` e `risk_level`  
- `explanation_layers`  
- `signals`  

Essa interpretação é sempre contextualizada pela matriz cultural 3×48.

---

# 📦 Estrutura de Diretórios (v0.5)

kaldra/
├── kernel/
│ └── bias/
│ ├── api/
│ │ └── main.py
│ │ └── api_spec.md
│ ├── data/
│ │ └── archetypes/
│ │ ├── delta12_archetypes.json
│ │ ├── delta144_grid.json
│ │ ├── cultural_3x48.json
│ │ └── locales_map.json
│ ├── datasets/
│ ├── examples/
│ ├── src/
│ │ ├── settings.py
│ │ ├── logging_config.py
│ │ ├── embeddings.py
│ │ ├── delta12.py
│ │ ├── delta144_mapping.py
│ │ ├── kindra_3x48.py
│ │ ├── scorer.py
│ │ ├── tau.py
│ │ ├── explain.py
│ │ └── pipeline.py
│ └── tests/
│ ├── test_api_v05.py
│ └── test_pipeline.py
├── docs/
├── README.md
├── pyproject.toml

---

# 📡 API – Versão v0.5

Endpoint principal:
POST /analyze

Envia um texto → retorna:
- score de viés  
- classificação de risco  
- arquétipo dominante  
- plano (3, 6 ou 9)  
- camadas narrativas do motor Pensadores  
- sinais culturais relevantes  

O endpoint `/health` está disponível para verificação simples.

---

# 🔬 Testes

Rodar os testes:
pytest -q

Todos os testes v0.5 cobrem:
- pipeline  
- embeddings determinísticos  
- camada de explicação  
- API FastAPI  
- arquivos de arquétipos  

---

# 🌍 Extensibilidade para KALDRA-Alpha, KALDRA-GEO e Kindra-for-Product

O design v0.5 foi criado para suportar expansão modular.

Cada novo kernel reutilizará:
- a malha de arquétipos (delta12 + delta144)  
- matriz cultural 3×48  
- motor Pensadores  
- estrutura de explicação  
- lógica de sinais  

Diferença entre eles:

| Módulo | Como usa a arquitetura v0.5 |
|--------|------------------------------|
| **KALDRA-Bias** | Interpreta textos buscando vieses narrativos. |
| **KALDRA-Alpha** | Analisa intenções, estilo narrativo e alinhamento de agentes. |
| **KALDRA-GEO** | Interpreta narrativas políticas, civilizacionais e geoculturais. |
| **Kindra-for-Product** | Mapeia produtos e marcas em arquétipos / cultura / narrativa. |

---

# 📜 Licença
MIT License.
