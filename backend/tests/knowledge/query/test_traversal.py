from uuid import uuid4

from app.knowledge.graph_model import EvidenceGraphEdge, EvidenceGraphNode
from app.knowledge.graph_types import GraphEdgeType, GraphNodeType
from app.knowledge.memory_repository import InMemoryEvidenceGraphRepository
from app.knowledge.query.traversal import EvidenceGraphTraversalQuery


def build_query():
    repository = InMemoryEvidenceGraphRepository()

    node_a = EvidenceGraphNode(
        id=uuid4(),
        node_type=GraphNodeType.EVIDENCE,
    )
    node_b = EvidenceGraphNode(
        id=uuid4(),
        node_type=GraphNodeType.CITATION,
    )
    node_c = EvidenceGraphNode(
        id=uuid4(),
        node_type=GraphNodeType.CLAIM,
    )

    repository.add_node(node_a)
    repository.add_node(node_b)
    repository.add_node(node_c)

    repository.add_edge(
        EvidenceGraphEdge(
            source_id=node_a.id,
            target_id=node_b.id,
            edge_type=GraphEdgeType.REFERENCES,
        )
    )
    repository.add_edge(
        EvidenceGraphEdge(
            source_id=node_b.id,
            target_id=node_c.id,
            edge_type=GraphEdgeType.SUPPORTS,
        )
    )

    return EvidenceGraphTraversalQuery(repository), node_a, node_b, node_c


def test_traverse_respects_depth_limit():
    query, node_a, node_b, node_c = build_query()

    result = query.traverse(node_a.id, depth=1)

    ids = {node.id for node in result}

    assert node_a.id in ids
    assert node_b.id in ids
    assert node_c.id not in ids


def test_traverse_returns_connected_nodes():
    query, node_a, node_b, node_c = build_query()

    result = query.traverse(node_a.id, depth=2)

    ids = {node.id for node in result}

    assert ids == {node_a.id, node_b.id, node_c.id}


def test_traverse_handles_cycles_without_looping():
    query, node_a, node_b, _ = build_query()

    query.repository.add_edge(
        EvidenceGraphEdge(
            source_id=node_b.id,
            target_id=node_a.id,
            edge_type=GraphEdgeType.DERIVED_FROM,
        )
    )

    result = query.traverse(node_a.id, depth=5)

    ids = [node.id for node in result]

    assert ids.count(node_a.id) == 1
