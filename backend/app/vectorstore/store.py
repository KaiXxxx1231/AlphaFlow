from typing import Any, Dict, List

from .base import VectorStore


class InMemoryVectorStore(VectorStore):
    """Development vector store implementation.

    A simple in-memory store used before integrating FAISS/Qdrant.
    """

    def __init__(self):
        self.vectors: Dict[str, Dict[str, Any]] = {}

    def add(
        self,
        vector_id: str,
        embedding: List[float],
        metadata: Dict[str, Any],
    ):
        self.vectors[vector_id] = {
            "embedding": embedding,
            "metadata": metadata,
        }

    def search(self, query_vector: List[float], top_k: int = 5):
        results = []
        for vector_id, item in self.vectors.items():
            results.append(
                {
                    "id": vector_id,
                    "score": self._similarity(query_vector, item["embedding"]),
                    "metadata": item["metadata"],
                }
            )

        return sorted(
            results,
            key=lambda item: item["score"],
            reverse=True,
        )[:top_k]

    def delete(self, vector_id: str):
        self.vectors.pop(vector_id, None)

    def _similarity(self, a: List[float], b: List[float]) -> float:
        if len(a) != len(b):
            return 0.0
        return sum(x * y for x, y in zip(a, b))
