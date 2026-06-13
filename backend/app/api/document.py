from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from backend.app.core.qdrant_client import client
from backend.app.services.pdf_service import extract_text_from_pdf
from backend.app.services.chunk_service import split_text_into_chunks
from backend.app.services.embedding_service import get_embeddings
from uuid import uuid4

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("/")
def get_document():
    return {"message": "Document API is working!"}

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_location = UPLOAD_DIR / file.filename
    with open(file_location, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    text = extract_text_from_pdf(file_location)
    chunks = split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200)
    # documents.clear()  # Clear existing documents before adding new ones
    
    points = []
    for chunk in chunks:
        embedding = get_embeddings(chunk)
        points.append(
            {
                "id": str(uuid4()),
                "vector": embedding.tolist(),
                "payload": {
                    "chunk": chunk
                }
            }
        )
    client.upsert(
        collection_name="knowledge_base",
        points=points
    )
    print("Documents uploaded successfully.")
    return {
        "filename": file.filename,
        "file_location": str(file_location),
        "num_chunks": len(chunks),
        "total_documents": len(chunks)
    }
