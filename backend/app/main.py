from fastapi import FastAPI
from backend.app.api.document import router as document_router
from backend.app.models.api_response import ApiResponse
from backend.app.models.question import QuestionRequest
from backend.app.services.rag_service import RagService
from backend.app.core.qdrant_client import client
from qdrant_client.models import VectorParams, Distance
from backend.app.core.dependencies import get_rag_service
from fastapi import Depends
from backend.app.core.exception_handler import document_not_found_exception_handler
from backend.app.exceptions.document_exception import DocumentNotFoundException
import backend.app.core.logger
from backend.app.core.settings import settings
from fastapi import status


print("---------------------------------------")
print(settings.database_name)

app = FastAPI(
    title="Enterprise Knowledge Assistant API",
    description="API for the Enterprise Knowledge Assistant application.",
    version="1.0.0",
)
app.add_exception_handler(DocumentNotFoundException,document_not_found_exception_handler)
# qdrant_repository = QdrantRepository(client)
# doc_repository = DocumentRepository()
# rag_service = RagService (qdrant_repository)
# doc_service = DocumentService(document_repository = doc_repository , qdrant_repository=qdrant_repository)

@app.on_event("startup")
def startup_event():
    collections = client.get_collections()
    collection_names = [collection.name for collection in collections.collections]
    if settings.collection_name not in collection_names:
        client.create_collection(
            collection_name=settings.collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )
    print("Qdrant client initialized and collection checked/created.")

app.include_router(document_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Enterprise Knowledge Assistant API"}
  
@app.post("/ask")
def ask_question(request: QuestionRequest, rag_service: RagService = Depends(get_rag_service),status_code=status.HTTP_200_OK):
    response = rag_service.answer_question(request.question, request.document_ids)
    result = {
        "question": request.question,
        "response": response}

    return ApiResponse(
        status=True,
        message="Question answered successfully",
        data=result
    )
