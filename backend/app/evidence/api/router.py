from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..models import Evidence
from ..storage import InMemoryEvidenceRepository


router = APIRouter(
    prefix="/evidence",
    tags=["evidence"],
)


repository = InMemoryEvidenceRepository()


@router.post("", response_model=Evidence)
def create_evidence(evidence: Evidence) -> Evidence:
    """Create an evidence record."""

    return repository.save(evidence)


@router.get("/{evidence_id}", response_model=Evidence)
def get_evidence(evidence_id: UUID) -> Evidence:
    """Retrieve evidence by id."""

    evidence = repository.get(evidence_id)

    if evidence is None:
        raise HTTPException(
            status_code=404,
            detail="Evidence not found",
        )

    return evidence


@router.get("", response_model=list[Evidence])
def list_evidence() -> list[Evidence]:
    """List stored evidence items."""

    return repository.list()
