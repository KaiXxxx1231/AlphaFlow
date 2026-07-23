from uuid import uuid4

from app.knowledge.graph_model import (
    EvidenceGraph,
    EvidenceGraphEdge,
    EvidenceGraphNode,
)
from app.knowledge.graph_types import (
    GraphEdgeType,
    GraphNodeType,
)


def test_evidence_graph_node_contract():
    node_id = uuid4()

    node = EvidenceGraphNode(
        id=node_id,
        node_type=GraphNodeType.EVIDENCE,
        metadata={
            "source": "document-1"
        },
    )

    assert node.id == node_id
    assert node.node_type == GraphNodeType.EVIDENCE
    assert node.metadata["source"] == "document-1"


def test_evidence_graph_edge_contract():
    source_id = uuid4()
    target_id = uuid4()

    edge = EvidenceGraphEdge(
        source_id=source_id,
        target_id=target_id,
        edge_type=GraphEdgeType.SUPPORTS,
    )

    assert edge.source_id == source_id
    assert edge.target_id == target_id
    assert edge.edge_type == GraphEdgeType.SUPPORTS


def test_evidence_graph_neighbor_traversal_contract():
    source = EvidenceGraphNode(
        id=uuid4(),
        node_type=GraphNodeType.DOCUMENT,
    )

    target = EvidenceGraphNode(
        id=uuid4(),
        node_type=GraphNodeType.EVIDENCE,
    )

    graph = EvidenceGraph()

    graph.add_node(source)
    graph.add_node(target)

    graph.add_edge(
        EvidenceGraphEdge(
            source_id=source.id,
            target_id=target.id,
            edge_type=GraphEdgeType.EXTRACTED_FROM,
        )
    )

    neighbors = graph.get_neighbors(source.id)

    assert len(neighbors) == 1
    assert neighbors[0].id == target.id


def test_evidence_graph_missing_node_is_ignored():
    graph = EvidenceGraph()

    graph.add_edge(
        EvidenceGraphEdge(
            source_id=uuid4(),
            target_id=uuid4(),
            edge_type=GraphEdgeType.SUPPORTS,
        )
    )

    assert graph.get_neighbors(uuid4()) == []
