from backend.app.repositories.document_repository import DocumentRepository
from backend.app.repositories.qdrant_repository import QdrantRepository
from backend.app.core.qdrant_client import client
from backend.app.services.document_service import DocumentService
from backend.app.services.rag_service import RagService
def get_document_repository():
  return DocumentRepository();

def get_qdrant_repository():
  return QdrantRepository(client);

def get_document_service():
  return DocumentService(
    document_repository =get_document_repository(),
    qdrant_repository=get_qdrant_repository()
  )

def get_rag_service():
  return RagService(
    qdrant_repository=get_qdrant_repository()
  )