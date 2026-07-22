import pytest

from backend.app.knowledge.query.exceptions import (
    GraphNodeNotFoundError,
    InvalidTraversalDepthError,
)
from backend.app.knowledge.query.traversal import EvidenceGraphTraversalQuery


class FakeRepository:
    def get_node(self, node_id):
        return None


class BrokenRepository:
    def get_node(self, node_id):
        raise RuntimeError("storage failure")


def test_traversal_invalid_depth():
    query = EvidenceGraphTraversalQuery(FakeRepository())

    with pytest.raises(InvalidTraversalDepthError):
        query.traverse("node-1", depth=0)


def test_traversal_node_not_found():
    query = EvidenceGraphTraversalQuery(FakeRepository())

    with pytest.raises(GraphNodeNotFoundError):
        query.traverse("missing-node", depth=1)


def test_repository_exception_isolated():
    query = EvidenceGraphTraversalQuery(BrokenRepository())

    with pytest.raises(GraphNodeNotFoundError):
        query.traverse("node-1", depth=1)
