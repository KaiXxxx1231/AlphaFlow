from uuid import UUID
from typing import List, Set

from ..graph_model import EvidenceGraphNode
from ..repository import EvidenceGraphRepository
from .exceptions import (
    GraphNodeNotFoundError,
    InvalidTraversalDepthError,
)


class EvidenceGraphTraversalQuery:
    """
    Read-only graph traversal query service.

    Provides bounded traversal over the evidence graph without coupling
    to a specific graph database implementation.
    """

    def __init__(self, repository: EvidenceGraphRepository) -> None:
        self.repository = repository

    def traverse(self, node_id: UUID, depth: int = 1) -> List[EvidenceGraphNode]:
        if depth < 1:
            raise InvalidTraversalDepthError(
                "Traversal depth must be greater than zero"
            )

        visited: Set[UUID] = set()
        result: List[EvidenceGraphNode] = []

        self._walk(
            node_id=node_id,
            remaining_depth=depth,
            visited=visited,
            result=result,
        )

        return result

    def _walk(
        self,
        node_id: UUID,
        remaining_depth: int,
        visited: Set[UUID],
        result: List[EvidenceGraphNode],
    ) -> None:
        if node_id in visited:
            return

        node = self.repository.get_node(node_id)
        if node is None:
            if not result:
                raise GraphNodeNotFoundError(
                    f"Graph node not found: {node_id}"
                )
            return

        visited.add(node_id)
        result.append(node)

        if remaining_depth == 0:
            return

        for neighbor in self.repository.get_neighbors(node_id):
            self._walk(
                node_id=neighbor.id,
                remaining_depth=remaining_depth - 1,
                visited=visited,
                result=result,
            )
