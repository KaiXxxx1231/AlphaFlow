from abc import ABC, abstractmethod
from typing import Any, Dict, List


class VectorStore(ABC):
    """Abstract vector storage interface."""

    @abstractmethod
    def add(self, vector_id: str, embedding: List[float], metadata: Dict[str, Any]):
        pass

    @abstractmethod
    def search(self, query_vector: List[float], top_k: int = 5):
        pass

    @abstractmethod
    def delete(self, vector_id: str):
        pass
