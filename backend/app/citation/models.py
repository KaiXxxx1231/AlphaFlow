from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Citation(BaseModel):
    """
    Traceability link between an evidence item and its source.

    Citation intentionally stays independent from storage and retrieval.
    It provides the foundation for evidence -> source reconstruction.
    """

    id: UUID = Field(default_factory=uuid4)

    evidence_id: UUID

    source_id: UUID

    source_type: str

    location: Optional[dict] = None

    reference_text: Optional[str] = None

    metadata: dict = Field(default_factory=dict)

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
