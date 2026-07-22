from typing import Optional
from uuid import UUID

from ..models import Citation
from .repository import CitationRepository


class InMemoryCitationRepository(CitationRepository):
    """
    In-memory citation repository.

    Used for development and testing before database adapters.
    """

    def __init__(self) -> None:
        self._items: dict[UUID, Citation] = {}

    def save(self, citation: Citation) -> Citation:
        self._items[citation.id] = citation
        return citation

    def get(self, citation_id: UUID) -> Optional[Citation]:
        return self._items.get(citation_id)

    def list(self) -> list[Citation]:
        return list(self._items.values())
