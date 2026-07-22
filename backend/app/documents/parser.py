from .models import Document


class DocumentParser:
    """Base parser pipeline for documents."""

    def parse(self, filename: str, content: str) -> Document:
        return Document(
            id=filename,
            filename=filename,
            content=content,
            metadata={"source": filename},
        )
