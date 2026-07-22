from typing import Dict, List
from uuid import UUID

from .graph_model import EvidenceGraphEdge, EvidenceGraphNode
from .repository import EvidenceGraphRepository


class InMemoryEvidenceGraphRepository(EvidenceGraphRepository):
    """
    In-memory graph repository adapter.
    """

    def __init__(self) -> None:
        self.nodes: Dict[UUID, EvidenceGraphNode] = {}
        self.edges: List[EvidenceGraphEdge] = []

    def add_node(self, node: EvidenceGraphNode) -> None:
        self.nodes[node.id] = node

    def add_edge(self, edge: EvidenceGraphEdge) -> None:
        self.edges.append(edge)

    def get_node(self, node_id: UUID) -> EvidenceGraphNode | None:
        return self.nodes.get(node_id)

    def get_neighbors(self, node_id: UUID) -> List[EvidenceGraphNode]:
        neighbor_ids = []

        for edge in self.edges:
            if edge.source_id == node_id:
                neighbor_ids.append(edge.target_id)
            elif edge.target_id == node_id:
                neighbor_ids.append(edge.source_id)

        return [
            self.nodes[item_id]
            for item_id in neighbor_ids
            if item_id in self.nodes
        ]
