from typing import Dict
from uuid import UUID

from pydantic import BaseModel, Field

from ...graph_types import GraphNodeType


class GraphTraversalNodeResponse(BaseModel):
    id: UUID
    node_type: GraphNodeType
    metadata: Dict = Field(default_factory=dict)


class GraphTraversalResponse(BaseModel):
    nodes: list[GraphTraversalNodeResponse]
    depth: int
