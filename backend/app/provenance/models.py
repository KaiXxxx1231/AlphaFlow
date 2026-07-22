from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ProvenanceEvent(str, Enum):
    EXTRACTED = "extracted"
    TRANSFORMED = "transformed"
    VERIFIED = "verified"
    LINKED = "linked"


class ProvenanceRecord(BaseModel):
    id: UUID = Field(default_factory=uuid4)

    source_id: UUID
    source_type: str

    target_id: UUID
    target_type: str

    event: ProvenanceEvent

    metadata: Dict[str, Any] = Field(default_factory=dict)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
