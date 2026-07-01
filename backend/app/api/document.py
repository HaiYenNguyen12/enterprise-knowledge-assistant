from fastapi import APIRouter, UploadFile, File
from backend.app.models.api_response import ApiResponse
from backend.app.models.document import UploadDocumentResponse
from backend.app.services.document_service import DocumentService
from fastapi import Depends
from backend.app.core.dependencies import get_document_service
from fastapi import status
# UPLOAD_DIR = Path("uploads")
# UPLOAD_DIR.mkdir(exist_ok=True)

# document_service = DocumentService(
#     document_repository=DocumentRepository(),
#     qdrant_repository=QdrantRepository(client)
# )

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("/",response_model=ApiResponse)
def get_document():
    return ApiResponse(
        status=True,
        message="Document API is working!"
    )

@router.post("/upload", response_model=ApiResponse, status_code=status.HTTP_201_CREATED )
async def upload_document(file: UploadFile = File(...), document_service: DocumentService = Depends(get_document_service)):
    result = await document_service.upload_document(file)
    upload_response = UploadDocumentResponse(**result)
    return ApiResponse(
        status=True,
        message="Document uploaded successfully",
        data=upload_response
    )   


@router.get("/all", response_model=ApiResponse, status_code=status.HTTP_200_OK)
def get_documents(document_service: DocumentService = Depends(get_document_service)):
    return ApiResponse(
        status=True,
        message="Documents retrieved successfully",
        data=document_service.get_documents()
    )

@router.delete("/{document_id}", response_model=ApiResponse,status_code=status.HTTP_200_OK)
def delete_document(document_id: str, 
                    document_service: DocumentService =  Depends(get_document_service)):
    document_service.delete_document(document_id);
    return ApiResponse(
        status=True,
        message="Document deleted successfully")
    

    
