"""Lightweight embedding utilities for the Bias kernel."""

from __future__ import annotations

import hashlib
import numpy as np

_EMBEDDING_SIZE = 384


def _hash_embedding(text: str) -> np.ndarray:
    """Generate a deterministic, normalized embedding vector from the input text.

    The implementation avoids external network calls so the test suite can run in
    restricted environments. The embedding length is fixed to ``_EMBEDDING_SIZE``
    and is derived from the SHA-256 digest of the text.
    """

    digest = hashlib.sha256(text.encode("utf-8")).digest()
    repeats = (_EMBEDDING_SIZE + len(digest) - 1) // len(digest)
    buffer = (digest * repeats)[:_EMBEDDING_SIZE]

    values = np.frombuffer(buffer, dtype=np.uint8).astype(np.float32)
    return values / 255.0


def get_embedding(text: str) -> list[float]:
    """Return a deterministic embedding vector for the provided text."""

    embedding = _hash_embedding(text)
    return embedding.tolist()
