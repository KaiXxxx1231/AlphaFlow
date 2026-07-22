from typing import Optional
from uuid import UUID

from ..models import Evidence
from .repository import EvidenceRepository


class InMemoryEvidenceRepository(EvidenceRepository):
    """
    In-memory evidence repository.

    Intended for development, testing, and early pipeline integration.
    Database implementations can replace this adapter later.
    """

    def __init__(self) -> None:
        self._items: dict[UUID, Evidence] = {}

    def save(self, evidence: Evidence) -> Evidence:
        self._items[evidence.id] = evidence
        return evidence

    def get(self, evidence_id: UUID) -> Optional[Evidence]:
        return self._items.get(evidence_id)

    def list(self) -> list[Evidence]:
        return list(self._items.values())
