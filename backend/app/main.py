from fastapi import FastAPI
from backend.app.api.document import router as document_router

app = FastAPI(
    title="Enterprise Knowledge Assistant API",
    description="API for the Enterprise Knowledge Assistant application.",
    version="1.0.0",
)

app.include_router(document_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Enterprise Knowledge Assistant API"}
  