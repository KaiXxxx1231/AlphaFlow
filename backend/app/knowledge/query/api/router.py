from uuid import UUID

from fastapi import APIRouter, Query

from ..traversal import EvidenceGraphTraversalQuery
from ...memory_repository import InMemoryEvidenceGraphRepository
from .schemas import GraphTraversalResponse, GraphTraversalNodeResponse


router = APIRouter(prefix="/knowledge/graph", tags=["graph"])


_repository = InMemoryEvidenceGraphRepository()
_query = EvidenceGraphTraversalQuery(repository=_repository)


@router.get(
    "/traversal/{node_id}",
    response_model=GraphTraversalResponse,
)
def traverse_graph(
    node_id: UUID,
    depth: int = Query(default=1, ge=0),
):
    nodes = _query.traverse(
        node_id=node_id,
        depth=depth,
    )

    return GraphTraversalResponse(
        nodes=[
            GraphTraversalNodeResponse(
                id=node.id,
                node_type=node.node_type,
                metadata=node.metadata,
            )
            for node in nodes
        ],
        depth=depth,
    )
