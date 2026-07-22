from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class CitationCreate(BaseModel):
    """Input schema for creating source traceability records."""

    evidence_id: UUID

    source_id: UUID

    source_type: str

    location: Optional[dict] = None

    reference_text: Optional[str] = None

    metadata: dict = {}
