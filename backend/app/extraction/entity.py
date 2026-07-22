from dataclasses import dataclass, field
from typing import List


@dataclass
class Entity:
    name: str
    entity_type: str
    mentions: int = 1
    metadata: dict = field(default_factory=dict)


class EntityExtractor:
    """Base entity extraction engine.

    Initial implementation uses simple rule matching.
    Replace with LLM/NLP providers in future iterations.
    """

    ENTITY_TYPES = [
        "Person",
        "Organization",
        "Location",
        "Technology",
        "Concept",
    ]

    def extract(self, text: str) -> List[Entity]:
        entities = []

        for keyword in ["AlphaFlow", "FastAPI", "Python"]:
            if keyword in text:
                entities.append(
                    Entity(
                        name=keyword,
                        entity_type="Technology",
                        mentions=text.count(keyword),
                    )
                )

        return entities
