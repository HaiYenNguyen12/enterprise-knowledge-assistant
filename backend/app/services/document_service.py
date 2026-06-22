from uuid import uuid4
from datetime import datetime
from backend.app.services.qdrant_client import client
from backend.app.services.pdf_service import extract_text_from_pdf
from backend.app.services.chunk_service import split_text_into_chunks
from backend.app.services.embedding_service import get_embeddings


class DocumentService:
    def __init__(self, document_repository, qdrant_repository):
        self.document_repository = document_repository
        self.qdrant_repository = qdrant_repository

    def upload_document(self, file):
      file_location = self._save_file(file)
      document_id = str(uuid4())
      self.document_repository.create_document(
         document_id=document_id,
         file_name=file.filename,
         file_path=file_location,
         file_size=file.size,
         created_at=datetime.now()
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
                      "chunk": chunk,
                      "source_file": file.filename
                  },
              }
          )





 