"""
Configuração de logging estruturado para o KALDRA-Bias.

- Usa loguru como backend.
- Nível de log e ambiente vêm de BiasSettings (settings.py).
- Fornece uma função get_logger() para uso consistente em todo o kernel.
"""

from __future__ import annotations

import sys
from typing import Optional

from loguru import logger as _logger

from .settings import get_settings


# Logger global já configurado com extras (app/env)
_LOGGER = _logger

_CONFIGURED: bool = False


def _configure_logger() -> None:
    """
    Aplica a configuração padrão do logger com base nas settings.

    - Remove handlers default do loguru.
    - Adiciona saída para stdout.
    - Usa nível vindo de settings, se disponível.
    """
    global _CONFIGURED, _LOGGER

    if _CONFIGURED:
        return

    # Remove qualquer configuração anterior
    _logger.remove()

    # Recupera settings (se disponíveis)
    level = "INFO"
    env: Optional[str] = None

    if get_settings is not None:
        settings = get_settings()
        level = settings.log_level
        env = settings.environment

    # Sink principal: stdout, formato estruturado
    _logger.add(
        sys.stdout,
        level=level,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "{extra[app]: <12} | "
            "{extra[env]: <8} | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
    )

    # Bind de campos padrão (AGORA armazenado em _LOGGER)
    _LOGGER = _logger.bind(app="kaldra-bias", env=env or "local")

    _CONFIGURED = True


def get_logger():
    """
    Retorna o logger global configurado.

    Uso típico:
        from kaldra.kernel.safeguard.src.logging_config import get_logger
        logger = get_logger()
        logger.info("mensagem")
    """
    if not _CONFIGURED:
        _configure_logger()
    return _LOGGER
