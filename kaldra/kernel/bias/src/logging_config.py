"""
KALDRA-CORE shim — módulo compartilhado.

Este arquivo mantém a API original do KALDRA-Bias,
reexportando o módulo equivalente a partir de `kaldra.kernel.core`.
"""
# Este shim reexporta a implementação de logging do core.
# A configuração específica (app="kaldra-bias", log_level)
# é gerenciada pelo pipeline do bias, que chama `get_settings`
# e reconfigura o logger se necessário. A interface `get_logger`
# permanece a mesma.

from kaldra.kernel.core.src.logging_config import *  # noqa: F401,F403
