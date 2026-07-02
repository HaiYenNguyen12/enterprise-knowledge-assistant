import math

from fastapi import APIRouter, UploadFile, File
from backend.app.models.api_response import ApiResponse
from backend.app.models.document import UploadDocumentResponse, DocumentResponse, DocumentsResponse, PaginationResponse
from backend.app.models.document import UploadDocumentResponse
from backend.app.services.document_service import DocumentService
from fastapi import Depends
from backend.app.core.dependencies import get_document_service
from fastapi import status
from fastapi import Query
from typing import Literal

# UPLOAD_DIR = Path("uploads")
# UPLOAD_DIR.mkdir(exist_ok=True)

# document_service = DocumentService(
#     document_repository=DocumentRepository(),
#     qdrant_repository=QdrantRepository(client)
# )

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("",response_model=ApiResponse, status_code=status.HTTP_200_OK)
def get_documents(
    keyword: str |None = Query(None, description="Search keywords for document file names"),
    sort_by: Literal["document_id", "file_name", "file_size", "created_at"] | None = Query("created_at", description="Field to sort by"),
    sort_order: Literal["asc", "desc"] | None = Query("desc", description="Sort order: 'asc' or 'desc'"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Number of documents per page"),
    document_service: DocumentService = Depends(get_document_service)
):
    documents,total_items = document_service.get_documents(
        keyword=keyword,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        page_size=page_size
    )
    return ApiResponse(
        status=True,
        message="Documents retrieved successfully",
        data=DocumentsResponse(
            items=documents,
            pagination=PaginationResponse(
                page=page,
                total_items=total_items,
                page_size=page_size,
                total_pages=math.ceil(total_items / page_size)
            )
        )
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

@router.delete("/{document_id}", response_model=ApiResponse,status_code=status.HTTP_200_OK)
def delete_document(document_id: str, 
                    document_service: DocumentService =  Depends(get_document_service)):
    document_service.delete_document(document_id);
    return ApiResponse(
        status=True,
        message="Document deleted successfully")
    

    
