from typing import Dict, List
from uuid import UUID

from app.provenance.models import ProvenanceRecord
from app.provenance.storage.repository import ProvenanceRepository


class InMemoryProvenanceRepository(ProvenanceRepository):
    """In-memory provenance repository adapter."""

    def __init__(self):
        self._records: Dict[UUID, ProvenanceRecord] = {}

    def save(self, record: ProvenanceRecord) -> ProvenanceRecord:
        self._records[record.id] = record
        return record

    def get(self, record_id: UUID) -> ProvenanceRecord | None:
        return self._records.get(record_id)

    def list(self) -> List[ProvenanceRecord]:
        return list(self._records.values())
