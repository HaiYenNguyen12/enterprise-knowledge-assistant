from pydantic import BaseModel


class UploadDocumentResponse(BaseModel):
    document_id: str
    filename: str
    file_location: str
    num_chunks: int


class DocumentResponse(BaseModel):
    document_id: str
    file_name: str
    file_size: int
    created_at: str