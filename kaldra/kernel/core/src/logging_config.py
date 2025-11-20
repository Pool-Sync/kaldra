"""
Configuração de logging estruturado para o KALDRA.

- Usa loguru como backend.
- Fornece uma função get_logger() para uso consistente em todo o kernel.
"""

from __future__ import annotations

import sys
from typing import Optional

from loguru import logger as _logger

# Logger global
_LOGGER = _logger

_CONFIGURED: bool = False


def _configure_logger() -> None:
    """
    Aplica a configuração padrão do logger.

    - Remove handlers default do loguru.
    - Adiciona saída para stdout.
    """
    global _CONFIGURED, _LOGGER

    if _CONFIGURED:
        return

    # Remove qualquer configuração anterior
    _logger.remove()

    level = "INFO"
    env: Optional[str] = "local"
    app_name: str = "kaldra-core"

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

    # Bind de campos padrão
    _LOGGER = _logger.bind(app=app_name, env=env)

    _CONFIGURED = True


def get_logger():
    """
    Retorna o logger global configurado.
    """
    if not _CONFIGURED:
        _configure_logger()
    return _LOGGER
