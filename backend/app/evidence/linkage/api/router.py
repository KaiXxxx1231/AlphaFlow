from uuid import UUID

from fastapi import APIRouter, HTTPException

from app.citation.models import Citation
from app.citation.service import CitationService
from app.citation.storage.memory import InMemoryCitationRepository
from app.evidence.storage.memory import InMemoryEvidenceRepository

from ..service import EvidenceCitationLinkageService


router = APIRouter(
    prefix="/evidence",
    tags=["evidence-linkage"],
)


citation_repository = InMemoryCitationRepository()
citation_service = CitationService(citation_repository)
evidence_repository = InMemoryEvidenceRepository()

linkage_service = EvidenceCitationLinkageService(
    evidence_repository,
    citation_service,
)


@router.post("/{evidence_id}/citations", response_model=Citation)
def link_citation(
    evidence_id: UUID,
    citation: Citation,
) -> Citation:
    """Link a citation to an evidence record."""

    try:
        return linkage_service.link(
            evidence_id,
            citation,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )


@router.get("/{evidence_id}/citations", response_model=list[Citation])
def list_evidence_citations(
    evidence_id: UUID,
) -> list[Citation]:
    """Retrieve citations associated with evidence."""

    return linkage_service.get_citations(evidence_id)
