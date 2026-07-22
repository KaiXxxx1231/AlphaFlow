from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from ..models import Citation


class CitationRepository(ABC):
    """
    Persistence contract for citation storage.

    Keeps citation domain independent from storage adapters.
    """

    @abstractmethod
    def save(self, citation: Citation) -> Citation:
        raise NotImplementedError

    @abstractmethod
    def get(self, citation_id: UUID) -> Optional[Citation]:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Citation]:
        raise NotImplementedError
