from fastapi import FastAPI
from backend.app.api.document import router as document_router
from backend.app.models.question import QuestionRequest
from backend.app.services.rag_service import answer_question
from backend.app.core.qdrant_client import client
from qdrant_client.models import VectorParams, Distance


app = FastAPI(
    title="Enterprise Knowledge Assistant API",
    description="API for the Enterprise Knowledge Assistant application.",
    version="1.0.0",
)

@app.on_event("startup")
def startup_event():
    collections = client.get_collections()
    collection_names = [collection.name for collection in collections.collections]
    if "knowledge_base" not in collection_names:
        client.create_collection(
            collection_name="knowledge_base",
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )
    print("Qdrant client initialized and collection checked/created.")

app.include_router(document_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Enterprise Knowledge Assistant API"}
  
@app.post("/ask")
def ask_question(request: QuestionRequest):
    response = answer_question(request.question)
    return {
        "question": request.question,
        "response": response}