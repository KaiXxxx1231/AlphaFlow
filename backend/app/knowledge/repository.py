from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from .graph_model import EvidenceGraphEdge, EvidenceGraphNode


class EvidenceGraphRepository(ABC):
    """
    Repository interface for Evidence Graph persistence.

    Keeps graph domain independent from storage implementation.
    """

    @abstractmethod
    def add_node(self, node: EvidenceGraphNode) -> None:
        pass

    @abstractmethod
    def add_edge(self, edge: EvidenceGraphEdge) -> None:
        pass

    @abstractmethod
    def get_node(self, node_id: UUID) -> EvidenceGraphNode | None:
        pass

    @abstractmethod
    def get_neighbors(self, node_id: UUID) -> List[EvidenceGraphNode]:
        pass
