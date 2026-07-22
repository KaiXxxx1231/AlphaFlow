from datetime import datetime
from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel

from .models import ProvenanceEvent


class ProvenanceCreate(BaseModel):
    source_id: UUID
    source_type: str

    target_id: UUID
    target_type: str

    event: ProvenanceEvent

    metadata: Dict[str, Any] = {}


class ProvenanceResponse(BaseModel):
    id: UUID

    source_id: UUID
    source_type: str

    target_id: UUID
    target_type: str

    event: ProvenanceEvent

    metadata: Dict[str, Any]

    created_at: datetime
