from fastapi import APIRouter, UploadFile, File
from backend.app.services.document_service import DocumentService
from fastapi import Depends
from backend.app.core.dependencies import get_document_service

# UPLOAD_DIR = Path("uploads")
# UPLOAD_DIR.mkdir(exist_ok=True)

# document_service = DocumentService(
#     document_repository=DocumentRepository(),
#     qdrant_repository=QdrantRepository(client)
# )

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("/")
def get_document():
    return {"message": "Document API is working!"}

@router.post("/upload")
async def upload_document(file: UploadFile = File(...), document_service: DocumentService = Depends(get_document_service)):
    return await document_service.upload_document(file)


@router.get("/all")
def get_documents(document_service: DocumentService = Depends(get_document_service)):
    return document_service.get_documents();

@router.delete("/{document_id}")
def delete_document(document_id: str, 
                    document_service: DocumentService =  Depends(get_document_service)):
    document_service.delete_document(document_id);
    return {
        "message" : "Document deleted successfully"
    }

    
