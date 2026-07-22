from dataclasses import dataclass, field
from typing import Dict, List

from .strategies import ChunkConfig


@dataclass
class Chunk:
    id: str
    content: str
    metadata: Dict[str, str] = field(default_factory=dict)


class TextChunker:
    """Split documents into overlapping text chunks."""

    def __init__(self, config: ChunkConfig | None = None):
        self.config = config or ChunkConfig()

    def split(self, text: str, document_id: str = "unknown") -> List[Chunk]:
        chunks = []
        start = 0
        index = 0

        while start < len(text):
            end = start + self.config.chunk_size
            content = text[start:end]

            chunks.append(
                Chunk(
                    id=f"{document_id}_chunk_{index}",
                    content=content,
                    metadata={"document_id": document_id},
                )
            )

            index += 1
            start = end - self.config.overlap

        return chunks
