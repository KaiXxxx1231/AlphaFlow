from app.knowledge.graph_model import GraphEdge, GraphNode
from app.knowledge.graph_types import GraphEdgeType, GraphNodeType
from app.knowledge.memory_repository import MemoryGraphRepository
from app.knowledge.query.traversal import EvidenceGraphTraversalQuery


def build_graph():
    repository = MemoryGraphRepository()

    repository.add_node(
        GraphNode(
            id="document-1",
            node_type=GraphNodeType.DOCUMENT,
            metadata={"name": "industrial-report"},
        )
    )

    repository.add_node(
        GraphNode(
            id="evidence-1",
            node_type=GraphNodeType.EVIDENCE,
            metadata={"content": "pressure anomaly detected"},
        )
    )

    repository.add_node(
        GraphNode(
            id="citation-1",
            node_type=GraphNodeType.CITATION,
            metadata={"page": 10},
        )
    )

    repository.add_node(
        GraphNode(
            id="claim-1",
            node_type=GraphNodeType.CLAIM,
            metadata={"statement": "equipment risk increased"},
        )
    )

    repository.add_edge(
        GraphEdge(
            source_id="document-1",
            target_id="evidence-1",
            edge_type=GraphEdgeType.CONTAINS,
        )
    )

    repository.add_edge(
        GraphEdge(
            source_id="evidence-1",
            target_id="citation-1",
            edge_type=GraphEdgeType.REFERENCES,
        )
    )

    repository.add_edge(
        GraphEdge(
            source_id="citation-1",
            target_id="claim-1",
            edge_type=GraphEdgeType.SUPPORTS,
        )
    )

    return repository


def test_traversal_depth_one():
    query = EvidenceGraphTraversalQuery(build_graph())

    result = query.traverse("document-1", depth=1)

    node_ids = {node.id for node in result.nodes}

    assert node_ids == {"document-1", "evidence-1"}


def test_traversal_multiple_depth():
    query = EvidenceGraphTraversalQuery(build_graph())

    result = query.traverse("document-1", depth=3)

    node_ids = {node.id for node in result.nodes}

    assert {
        "document-1",
        "evidence-1",
        "citation-1",
        "claim-1",
    }.issubset(node_ids)


def test_traversal_cycle_protection():
    repository = build_graph()

    repository.add_edge(
        GraphEdge(
            source_id="claim-1",
            target_id="document-1",
            edge_type=GraphEdgeType.DERIVED_FROM,
        )
    )

    query = EvidenceGraphTraversalQuery(repository)

    result = query.traverse("document-1", depth=10)

    node_ids = [node.id for node in result.nodes]

    assert len(node_ids) == len(set(node_ids))
