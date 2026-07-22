from typing import Dict, List
from uuid import UUID

from pydantic import BaseModel, Field

from .graph_types import GraphEdgeType, GraphNodeType


class EvidenceGraphNode(BaseModel):
    id: UUID
    node_type: GraphNodeType
    metadata: dict = Field(default_factory=dict)


class EvidenceGraphEdge(BaseModel):
    source_id: UUID
    target_id: UUID
    edge_type: GraphEdgeType
    metadata: dict = Field(default_factory=dict)


class EvidenceGraph(BaseModel):
    nodes: Dict[UUID, EvidenceGraphNode] = Field(default_factory=dict)
    edges: List[EvidenceGraphEdge] = Field(default_factory=list)

    def add_node(self, node: EvidenceGraphNode) -> None:
        self.nodes[node.id] = node

    def add_edge(self, edge: EvidenceGraphEdge) -> None:
        self.edges.append(edge)

    def get_neighbors(self, node_id: UUID) -> List[EvidenceGraphNode]:
        neighbor_ids = []

        for edge in self.edges:
            if edge.source_id == node_id:
                neighbor_ids.append(edge.target_id)
            elif edge.target_id == node_id:
                neighbor_ids.append(edge.source_id)

        return [
            self.nodes[node_id]
            for node_id in neighbor_ids
            if node_id in self.nodes
        ]
