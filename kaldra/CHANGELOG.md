# KALDRA – CHANGELOG

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
e este projeto segue versionamento semântico.

---

## [0.5.0] – 2025-11-18

**Estado:** Estável  
**Escopo:** Consolidação do kernel KALDRA-Bias com o motor “Pensadores” e preparação
para extensão futura aos demais módulos (KALDRA-Alpha, KALDRA-GEO, Kindra-for-Product).

### Adicionado
- **Camada de dados de arquétipos (v0.5):**
  - `kaldra/kernel/bias/data/archetypes/delta12_archetypes.json`  
  - `kaldra/kernel/bias/data/archetypes/delta144_grid.json`  
  - `kaldra/kernel/bias/data/archetypes/cultural_3x48.json`  
  - `kaldra/kernel/bias/data/archetypes/locales_map.json`  
  Esses arquivos definem a malha de arquétipos *delta12*, a grade 12×12 (*delta144*),
  o painel cultural 3×48 (Kindras) e o mapeamento de localidades/idiomas.

- **Motor “Pensadores” para contexto de bias:**
  - Integração explícita dos eixos de interpretação inspirados em quatro pensadores:
    - **Nietzsche** – Vontade de potência, ressentimento e inversões de valor.  
    - **Jung** – Arquétipos, sombra, anima/animus e inconsciente coletivo.  
    - **Campbell** – Jornada do herói, estágios narrativos e papéis míticos.  
    - **Marcus Aurelius** – Perspectiva estoica, disciplina e contenção ética.
  - A interpretação de bias agora é feita sobre **camadas de leitura** que combinam:
    - Score quantitativo de viés.  
    - Arquétipo dominante (delta12 / delta144).  
    - Posição na matriz cultural 3×48.  
    - Comentário narrativo baseado nos “Pensadores”.

- **Estrutura de diretórios v0.5 para o kernel Bias:**
  - Normalização da árvore em:
    - `kaldra/kernel/bias/api/` – FastAPI, endpoints e especificação (`api_spec.md`).  
    - `kaldra/kernel/bias/src/` – lógica de embeddings, pipeline, scorer, tau, explain, settings.  
    - `kaldra/kernel/bias/tests/` – testes unitários (`test_api_v05.py`, `test_pipeline.py`).  
    - `kaldra/kernel/bias/data/` – datasets e arquivos de arquétipos (ver seção acima).  
  - Documentação da estrutura em `kaldra/README.md` (seção “Estrutura de Diretórios (v0.5)”).

- **Camada de explicação (Explain Layers v0.5):**
  - Ampliação da resposta da API para incluir:
    - `dominant_archetype`  
    - `plan` (3, 6 ou 9)  
    - `archetype_detail`  
    - `explanation_layers`  
    - `signals`
  - Essas camadas são derivadas do motor “Pensadores” aplicado sobre os arquétipos
    e sobre a malha cultural.

- **Ambiente de testes e desenvolvimento:**
  - Padronização do uso de `pytest -q` como suíte mínima de regressão.  
  - Atualização do `pyproject.toml` para refletir dependências do kernel Bias v0.5.

### Modificado
- **Embeddings sem dependência externa de rede:**
  - Substituição do uso direto de `SentenceTransformer` por um mecanismo determinístico
    de embeddings baseado em hash, compatível com ambientes sem acesso à internet.
  - Objetivo: garantir reprodutibilidade e facilitar execução em pipelines fechados.

- **Imports do kernel Bias em modo pacote:**
  - Ajuste dos imports em `api/main.py`, `src/pipeline.py`, `src/train.py`,
    `tests/test_api_v05.py` e arquivos relacionados para que o kernel funcione
    corretamente quando instalado como pacote (`kaldra.kernel.bias`).

- **Configuração de logging:**
  - Simplificação de `logging_config.py` para uso de imports relativos estáveis.  
  - Preparação para futura integração com sistemas externos de observabilidade.

- **Documentação v0.5:**
  - Atualização de `kaldra/README.md` para refletir:
    - O escopo atual: **KALDRA-Bias** como primeiro kernel operacional.  
    - A presença dos arquivos de arquétipos e da matriz 3×48.  
    - A visão de evolução futura para KALDRA-Alpha, KALDRA-GEO e Kindra-for-Product.

### Removido
- **Arquivos de build e cache do repositório:**
  - Removidos arquivos `kaldra-egg-info` previamente versionados.  
  - Adicionado `.gitignore` em `kaldra/` cobrindo:
    - `__pycache__/`  
    - `*.pyc`  
    - `.pytest_cache/`  
    - `*.egg-info/`

### Notas sobre extensibilidade
- O design do motor “Pensadores” e da malha de arquétipos foi feito para ser
  **reutilizado** nos futuros núcleos:
  - **KALDRA-Alpha** – foco em alinhamento e narrativas de agentes.  
  - **KALDRA-GEO** – foco em leitura geopolítica e variação cultural por região.  
  - **Kindra-for-Product** – foco em arquétipos aplicados a produtos, marcas e UX.
- Nesta v0.5, a implementação é **totalmente operacional apenas para KALDRA-Bias**,
  mas a documentação já espelha a arquitetura comum futura.

---

## [0.4.0] – 2025-11-xx

- Versão anterior do kernel Bias, com:
  - Pipeline de bias score sem camadas de arquétipos formalizadas em arquivos JSON.  
  - Estrutura de diretórios menos organizada e sem separação clara de dados de arquétipos.  
  - Resposta da API com campos básicos de score e label, sem o motor “Pensadores”.

---

## [0.1.0] – 2025-11-xx

- Versão inicial de experimentação do KALDRA-Bias.
- Protótipo de pipeline de detecção de vieses textuais.
