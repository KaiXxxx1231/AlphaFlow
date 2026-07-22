from uuid import UUID

from .models import Evidence
from .storage import EvidenceRepository


class EvidenceService:
    """
    Application service for evidence operations.

    Keeps API transport separate from domain persistence.
    """

    def __init__(self, repository: EvidenceRepository):
        self.repository = repository

    def create(self, evidence: Evidence) -> Evidence:
        return self.repository.save(evidence)

    def get(self, evidence_id: UUID) -> Evidence | None:
        return self.repository.get(evidence_id)

    def list(self) -> list[Evidence]:
        return self.repository.list()
