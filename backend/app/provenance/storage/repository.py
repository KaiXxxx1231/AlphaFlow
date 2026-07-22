from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.provenance.models import ProvenanceRecord


class ProvenanceRepository(ABC):
    """Repository interface for provenance persistence."""

    @abstractmethod
    def save(self, record: ProvenanceRecord) -> ProvenanceRecord:
        pass

    @abstractmethod
    def get(self, record_id: UUID) -> ProvenanceRecord | None:
        pass

    @abstractmethod
    def list(self) -> List[ProvenanceRecord]:
        pass
