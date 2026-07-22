from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from ..models import Evidence


class EvidenceRepository(ABC):
    """
    Persistence contract for evidence storage.

    Domain services depend on this interface instead of a concrete database.
    """

    @abstractmethod
    def save(self, evidence: Evidence) -> Evidence:
        raise NotImplementedError

    @abstractmethod
    def get(self, evidence_id: UUID) -> Optional[Evidence]:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Evidence]:
        raise NotImplementedError
