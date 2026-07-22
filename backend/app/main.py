from fastapi import FastAPI

from app.citation.api.router import router as citation_router


app = FastAPI(title="AlphaFlow API")


app.include_router(
    citation_router
)


@app.get("/")
def root():
    return {"name": "AlphaFlow", "status": "running"}
