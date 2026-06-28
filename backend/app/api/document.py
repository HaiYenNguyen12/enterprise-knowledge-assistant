from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from backend.app.core.qdrant_client import client
from backend.app.services.document_service import DocumentService
from backend.app.repositories.qdrant_repository import QdrantRepository
from backend.app.repositories.document_repository import DocumentRepository


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

document_service = DocumentService(
    document_repository=DocumentRepository(),
    qdrant_repository=QdrantRepository(client)
)

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("/")
def get_document():
    return {"message": "Document API is working!"}

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return await document_service.upload_document(file)


@router.get("/all")
def get_documents():
    return document_service.get_documents();

@router.delete("/{document_id}")
def delete_document(document_id):
    document_service.delete_document(document_id);
    return {
        "message" : "Document deleted successfully"
    }

    
