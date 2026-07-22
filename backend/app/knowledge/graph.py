from typing import Dict, List

from .schema import KnowledgeEdge, KnowledgeNode


class KnowledgeGraph:
    """Lightweight graph engine for development.

    Designed to be replaced by Neo4j or another graph database later.
    """

    def __init__(self):
        self.nodes: Dict[str, KnowledgeNode] = {}
        self.edges: List[KnowledgeEdge] = []

    def add_node(self, node: KnowledgeNode):
        self.nodes[node.id] = node

    def add_edge(self, edge: KnowledgeEdge):
        self.edges.append(edge)

    def query_neighbors(self, node_id: str):
        neighbors = []

        for edge in self.edges:
            if edge.source == node_id:
                neighbors.append(edge.target)
            elif edge.target == node_id:
                neighbors.append(edge.source)

        return neighbors
