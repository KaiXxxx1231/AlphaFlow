from uuid import UUID

from .models import ProvenanceRecord
from .storage.repository import ProvenanceRepository


class ProvenanceService:
    """
    Application service for provenance management.

    Coordinates provenance creation and retrieval while keeping
    persistence details behind repository abstraction.
    """

    def __init__(
        self,
        repository: ProvenanceRepository,
    ):
        self.repository = repository

    def create(
        self,
        record: ProvenanceRecord,
    ) -> ProvenanceRecord:
        return self.repository.save(record)

    def get(
        self,
        record_id: UUID,
    ) -> ProvenanceRecord | None:
        return self.repository.get(record_id)

    def list(self) -> list[ProvenanceRecord]:
        return self.repository.list()

    def find_by_source(
        self,
        source_id: UUID,
    ) -> list[ProvenanceRecord]:
        return [
            record
            for record in self.repository.list()
            if record.source_id == source_id
        ]

    def find_by_target(
        self,
        target_id: UUID,
    ) -> list[ProvenanceRecord]:
        return [
            record
            for record in self.repository.list()
            if record.target_id == target_id
        ]
