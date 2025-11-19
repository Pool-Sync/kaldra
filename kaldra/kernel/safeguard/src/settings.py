"""
Settings do kernel KALDRA-Bias.

Centraliza configuração básica:
- ambiente
- nível de log
- backend de embeddings
- limites de batch
- limites de tamanho de texto
- plano 3-6-9 padrão

Não depende de libs externas (só stdlib) para evitar acoplamento desnecessário.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from typing import Literal


PlanType = Literal[3, 6, 9]


@dataclass
class BiasSettings:
    """
    Configurações principais do KALDRA-Bias.

    Valores podem ser sobrescritos por variáveis de ambiente.
    """

    # Ambiente de execução
    environment: str = os.getenv("KALDRA_BIAS_ENV", "local")  # local | dev | prod

    # Nível de log (será usado pelo módulo de logging estruturado na v0.5)
    log_level: str = os.getenv("KALDRA_BIAS_LOG_LEVEL", "INFO")

    # Backend de embeddings (será conectado na etapa de EMBEDDINGS da v0.5)
    # Opções-alvo: "minilm", "e5-small", "jina"
    embedding_backend: str = os.getenv("KALDRA_BIAS_EMBEDDING_BACKEND", "minilm")

    # Limites de batch para analyze_batch()
    batch_max_items: int = int(os.getenv("KALDRA_BIAS_BATCH_MAX_ITEMS", "64"))

    # Limite de tamanho de texto (caracteres) para proteger a pipeline
    text_max_length_chars: int = int(
        os.getenv("KALDRA_BIAS_TEXT_MAX_LENGTH_CHARS", "8000")
    )

    # Plano 3-6-9 padrão (usado quando não houver contexto explícito)
    default_plan: PlanType = int(os.getenv("KALDRA_BIAS_DEFAULT_PLAN", "6"))  # type: ignore[assignment]


@lru_cache(maxsize=1)
def get_settings() -> BiasSettings:
    """
    Retorna instância única de BiasSettings (cacheada).

    Uso típico:
        from kaldra.kernel.safeguard.src.settings import get_settings
        settings = get_settings()
    """
    return BiasSettings()
