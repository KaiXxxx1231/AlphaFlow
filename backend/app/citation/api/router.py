from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..models import Citation
from ..service import CitationService
from ..storage.memory import InMemoryCitationRepository


router = APIRouter(
    prefix="/citations",
    tags=["citation"],
)


repository = InMemoryCitationRepository()
service = CitationService(repository)


@router.post("", response_model=Citation)
def create_citation(citation: Citation) -> Citation:
    """Create a citation record."""

    return service.create(citation)


@router.get("/{citation_id}", response_model=Citation)
def get_citation(citation_id: UUID) -> Citation:
    """Retrieve citation by id."""

    citation = service.get(citation_id)

    if citation is None:
        raise HTTPException(
            status_code=404,
            detail="Citation not found",
        )

    return citation


@router.get("", response_model=list[Citation])
def list_citations() -> list[Citation]:
    """List citation records."""

    return service.list()


@router.get("/evidence/{evidence_id}", response_model=list[Citation])
def get_evidence_citations(
    evidence_id: UUID,
) -> list[Citation]:
    """Retrieve citations linked to evidence."""

    return service.find_by_evidence(evidence_id)
