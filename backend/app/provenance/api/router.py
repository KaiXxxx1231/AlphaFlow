from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..models import ProvenanceRecord
from ..service import ProvenanceService
from ..storage.memory import InMemoryProvenanceRepository


router = APIRouter(
    prefix="/provenance",
    tags=["provenance"],
)


repository = InMemoryProvenanceRepository()
service = ProvenanceService(repository)


@router.post("", response_model=ProvenanceRecord)
def create_provenance(
    record: ProvenanceRecord,
) -> ProvenanceRecord:
    """Create a provenance record."""

    return service.create(record)


@router.get("/{record_id}", response_model=ProvenanceRecord)
def get_provenance(
    record_id: UUID,
) -> ProvenanceRecord:
    """Retrieve provenance record by id."""

    record = service.get(record_id)

    if record is None:
        raise HTTPException(
            status_code=404,
            detail="Provenance record not found",
        )

    return record


@router.get("", response_model=list[ProvenanceRecord])
def list_provenance() -> list[ProvenanceRecord]:
    """List provenance records."""

    return service.list()


@router.get("/source/{source_id}", response_model=list[ProvenanceRecord])
def get_source_provenance(
    source_id: UUID,
) -> list[ProvenanceRecord]:
    """Retrieve provenance records by source entity."""

    return service.find_by_source(source_id)


@router.get("/target/{target_id}", response_model=list[ProvenanceRecord])
def get_target_provenance(
    target_id: UUID,
) -> list[ProvenanceRecord]:
    """Retrieve provenance records by target entity."""

    return service.find_by_target(target_id)
