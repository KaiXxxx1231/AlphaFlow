from fastapi import FastAPI

from app.citation.api.router import router as citation_router
from app.provenance.api.router import router as provenance_router
from app.evidence.linkage.api.router import router as evidence_linkage_router
from app.evidence.lineage.api.router import router as evidence_lineage_router


app = FastAPI(title="AlphaFlow API")


app.include_router(
    citation_router
)

app.include_router(
    provenance_router
)

app.include_router(
    evidence_linkage_router
)

app.include_router(
    evidence_lineage_router
)


@app.get("/")
def root():
    return {"name": "AlphaFlow", "status": "running"}
