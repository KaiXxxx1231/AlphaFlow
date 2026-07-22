from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Document:
    id: str
    filename: str
    content: str
    metadata: Dict[str, str] = field(default_factory=dict)
