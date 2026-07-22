from uuid import UUID

from fastapi import APIRouter

from ..service import EvidenceLineageQueryService


router = APIRouter(
    prefix="/evidence",
    tags=["evidence-lineage"],
)


lineage_service = EvidenceLineageQueryService()


@router.get("/{evidence_id}/lineage")
def get_evidence_lineage(
    evidence_id: UUID,
):
    """Retrieve evidence lineage trace."""

    return lineage_service.get_lineage(str(evidence_id))
