from typing import Any


class EvidenceLineageQueryService:
    """
    Query service for evidence traceability.

    Aggregates lineage information across evidence, citation,
    provenance and graph relationships.
    """

    def __init__(
        self,
        evidence_repository=None,
        citation_service=None,
        provenance_service=None,
        graph_service=None,
    ):
        self.evidence_repository = evidence_repository
        self.citation_service = citation_service
        self.provenance_service = provenance_service
        self.graph_service = graph_service

    def get_lineage(self, evidence_id: str) -> dict[str, Any]:
        return {
            "evidence_id": evidence_id,
            "citations": self._get_citations(evidence_id),
            "provenance": self._get_provenance(evidence_id),
            "graph": self._get_graph(evidence_id),
        }

    def _get_citations(self, evidence_id: str):
        if self.citation_service is None:
            return []

        return self.citation_service.find_by_evidence(evidence_id)

    def _get_provenance(self, evidence_id: str):
        if self.provenance_service is None:
            return []

        return self.provenance_service.find_by_target(evidence_id)

    def _get_graph(self, evidence_id: str):
        if self.graph_service is None:
            return []

        return self.graph_service.get_neighbors(evidence_id)
