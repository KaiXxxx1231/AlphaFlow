from enum import Enum


class GraphNodeType(str, Enum):
    DOCUMENT = "document"
    CHUNK = "chunk"
    EVIDENCE = "evidence"
    CITATION = "citation"
    CLAIM = "claim"


class GraphEdgeType(str, Enum):
    CONTAINS = "contains"
    EXTRACTED_FROM = "extracted_from"
    SUPPORTS = "supports"
    REFERENCES = "references"
    DERIVED_FROM = "derived_from"
