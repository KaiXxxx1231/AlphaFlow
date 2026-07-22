from dataclasses import dataclass


@dataclass
class ChunkConfig:
    chunk_size: int = 1000
    overlap: int = 200
