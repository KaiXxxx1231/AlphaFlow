from pathlib import Path


class DocumentLoader:
    """Load raw document content from local files."""

    def load(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")
