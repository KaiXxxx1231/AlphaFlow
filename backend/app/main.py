from fastapi import FastAPI

app = FastAPI(title="AlphaFlow API")


@app.get("/")
def root():
    return {"name": "AlphaFlow", "status": "running"}
