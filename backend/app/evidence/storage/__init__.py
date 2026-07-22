"""
Evidence persistence layer.

Contains repository abstractions and storage adapters.
"""

from .repository import EvidenceRepository
from .memory import InMemoryEvidenceRepository

__all__ = [
    "EvidenceRepository",
    "InMemoryEvidenceRepository",
]
