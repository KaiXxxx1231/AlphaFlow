from uuid import UUID

from app.knowledge.graph_model import EvidenceGraph
from app.knowledge.graph_types import (
    GraphEdge,
    GraphNode,
    GraphNodeType,
)
from app.knowledge.repository import EvidenceGraphRepository


class EvidenceGraphService:
    """
    Application service for Evidence Graph operations.

    Responsible for graph orchestration:
    - node creation
    - edge creation
    - graph traversal queries

    Persistence concerns are delegated to repository.
    """

    def __init__(
        self,
        repository: EvidenceGraphRepository,
    ):
        self.repository = repository

    def add_node(
        self,
        node: GraphNode,
    ) -> GraphNode:
        """Add a graph node."""
        self.repository.add_node(node)
        return node

    def get_node(
        self,
        node_id: UUID,
    ) -> GraphNode | None:
        """Retrieve node by id."""
        return self.repository.get_node(node_id)

    def remove_node(
        self,
        node_id: UUID,
    ) -> None:
        """Remove graph node."""
        self.repository.remove_node(node_id)

    def add_edge(
        self,
        edge: GraphEdge,
    ) -> GraphEdge:
        """Add graph relationship."""
        self.repository.add_edge(edge)
        return edge

    def get_neighbors(
        self,
        node_id: UUID,
        node_type: GraphNodeType | None = None,
    ) -> list[GraphNode]:
        """Query adjacent nodes."""
        neighbors = self.repository.get_neighbors(node_id)

        if node_type is None:
            return neighbors

        return [
            node
            for node in neighbors
            if node.type == node_type
        ]

    def get_graph(self) -> EvidenceGraph:
        """Return current graph snapshot."""
        return self.repository.get_graph()
