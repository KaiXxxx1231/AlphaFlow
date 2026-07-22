from dataclasses import dataclass


@dataclass
class Relation:
    source: str
    target: str
    relation_type: str


class RelationExtractor:
    """Base relation extraction placeholder."""

    def extract(self, entities):
        relations = []

        for index in range(len(entities) - 1):
            relations.append(
                Relation(
                    source=entities[index].name,
                    target=entities[index + 1].name,
                    relation_type="related_to",
                )
            )

        return relations
