from typing import List

from .base import EmbeddingProvider


class MockEmbeddingProvider(EmbeddingProvider):
    """Development embedding provider placeholder.

    Replace with OpenAI or local model implementations later.
    """

    def embed(self, text: str) -> List[float]:
        return [float(len(text))]
