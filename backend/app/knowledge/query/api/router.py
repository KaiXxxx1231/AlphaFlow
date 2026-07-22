from uuid import UUID

from fastapi import APIRouter, Query

from ..traversal import EvidenceGraphTraversalQuery
from ...memory_repository import InMemoryEvidenceGraphRepository


router = APIRouter(prefix="/knowledge/graph", tags=["graph"])


_repository = InMemoryEvidenceGraphRepository()
_query = EvidenceGraphTraversalQuery(repository=_repository)


@router.get("/traversal/{node_id}")
def traverse_graph(
    node_id: UUID,
    depth: int = Query(default=1, ge=0),
):
    return _query.traverse(
        node_id=node_id,
        depth=depth,
    )
