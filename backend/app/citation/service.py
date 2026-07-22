from uuid import UUID

from .models import Citation
from .storage.repository import CitationRepository


class CitationService:
    """
    Application service for citation management.

    Coordinates citation creation and retrieval while keeping
    persistence details behind repository abstraction.
    """

    def __init__(
        self,
        repository: CitationRepository,
    ):
        self.repository = repository

    def create(
        self,
        citation: Citation,
    ) -> Citation:
        return self.repository.save(citation)

    def get(
        self,
        citation_id: UUID,
    ) -> Citation | None:
        return self.repository.get(citation_id)

    def list(self) -> list[Citation]:
        return self.repository.list()

    def find_by_evidence(
        self,
        evidence_id: UUID,
    ) -> list[Citation]:
        return [
            citation
            for citation in self.repository.list()
            if citation.evidence_id == evidence_id
        ]
