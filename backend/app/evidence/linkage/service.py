from uuid import UUID

from app.citation.models import Citation
from app.citation.service import CitationService
from app.evidence.models import Evidence
from app.evidence.storage.repository import EvidenceRepository


class EvidenceCitationLinkageService:
    """
    Coordinates Evidence and Citation relationships.

    Provides a domain service boundary for traceability between
    extracted evidence and source citations.
    """

    def __init__(
        self,
        evidence_repository: EvidenceRepository,
        citation_service: CitationService,
    ):
        self.evidence_repository = evidence_repository
        self.citation_service = citation_service

    def link(
        self,
        evidence_id: UUID,
        citation: Citation,
    ) -> Citation:
        evidence = self.evidence_repository.get(evidence_id)

        if evidence is None:
            raise ValueError("Evidence not found")

        if citation.evidence_id != evidence_id:
            raise ValueError("Citation evidence_id mismatch")

        return self.citation_service.create(citation)

    def get_citations(
        self,
        evidence_id: UUID,
    ) -> list[Citation]:
        return self.citation_service.find_by_evidence(evidence_id)
