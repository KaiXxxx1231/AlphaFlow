from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class KnowledgeNode:
    id: str
    name: str
    node_type: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class KnowledgeEdge:
    source: str
    target: str
    relation: str
    metadata: Dict[str, Any] = field(default_factory=dict)
