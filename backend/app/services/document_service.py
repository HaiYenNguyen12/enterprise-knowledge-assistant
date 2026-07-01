from uuid import uuid4
from datetime import datetime
from pathlib import Path
from backend.app.models.document import DocumentResponse
from backend.app.services.pdf_service import extract_text_from_pdf
from backend.app.services.chunk_service import split_text_into_chunks
from backend.app.services.embedding_service import get_embeddings
from fastapi import UploadFile
from backend.app.core.settings import settings
from backend.app.exceptions.document_exception import DocumentNotFoundException
import logging

logger = logging.getLogger(__name__)

class DocumentService:
    def __init__(self, document_repository, qdrant_repository):
        self.document_repository = document_repository
        self.qdrant_repository = qdrant_repository

    async def upload_document(self, file: UploadFile):
      file_location = None
      document_id = None
      try:
        file_location = await self._save_file(file)
        # raise Exception("Test logging")
        document_id = str(uuid4())
        size = Path(file_location).stat().st_size
        self.document_repository.create_document(
          document_id=document_id,
          file_name=file.filename,
          file_path=str(file_location),
          file_size=size,
          created_at=datetime.now().isoformat()
        )

        text = extract_text_from_pdf(file_location)
        chunks = split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200)
        points = []
        for chunk in chunks:
            embedding = get_embeddings(chunk)
            points.append(
                  {
                      "id": str(uuid4()),
                      "vector": embedding.tolist(),
                      "payload": {
                          "document_id": document_id,
                          "chunk": chunk,
                          "source_file": file.filename
                      }
                  }
              )
        self.qdrant_repository.upsert_chunks(points)
      except Exception:
          if document_id:
            self.document_repository.delete_document(document_id)
          if file_location and Path(file_location).exists():
              Path(file_location).unlink()
          logger.exception("Failed to upload document")

          raise 
      return {
          "document_id": document_id,
          "filename": file.filename,
          "file_location": str(file_location),
          "num_chunks": len(chunks)
      }
    
    def get_documents(self):
        documents = self.document_repository.get_documents();
        return [DocumentResponse(**doc) for doc in documents]

    def delete_document(self,document_id):
        document = self.document_repository.get_document_by_id(document_id)
        if document is None:
            # raise ValueError(f"Document '{document_id}' not found")
            raise DocumentNotFoundException(document_id)
        # try:
        self.qdrant_repository.delete_chunks_by_document_id(document_id)
        Path(document["file_path"]).unlink(missing_ok=True)
        self.document_repository.delete_document(document_id)
        # except Exception as e:
            # logger.exception("Failed to delete document")
            # raise





    async def _save_file(self, file):
        UPLOAD_DIR = Path(settings.upload_folder)
        UPLOAD_DIR.mkdir(exist_ok=True)
        file_location = UPLOAD_DIR / file.filename    
        with open(file_location, "wb") as buffer:
            content = await file.read()
            buffer.write(content) 
        return file_location    
 