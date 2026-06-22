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

    # file_location = UPLOAD_DIR / file.filename
    # with open(file_location, "wb") as buffer:
    #     content = await file.read()
    #     buffer.write(content)

    # text = extract_text_from_pdf(file_location)
    # chunks = split_text_into_chunks(text, chunk_size=1000, chunk_overlap=200)
    # # documents.clear()  # Clear existing documents before adding new ones
    
    # points = []
    # for chunk in chunks:
    #     embedding = get_embeddings(chunk)
    #     points.append(
    #         {
    #             "id": str(uuid4()),
    #             "vector": embedding.tolist(),
    #             "payload": {
    #                 "chunk": chunk,
    #                 "source_file": file.filename
    #             },
                

    #         }
    #     )
    # client.upsert(
    #     collection_name="knowledge_base",
    #     points=points
    # )
    # result = client.query_points(
    #     collection_name="knowledge_base",
    #     query_vector=get_embeddings("What is the capital of France?").tolist(),
    #     limit=1)
    # print("Query result:", result.points[0].payload)

    # print("Documents uploaded successfully.")
    # return {
    #     "filename": file.filename,
    #     "file_location": str(file_location),
    #     "num_chunks": len(chunks),
    #     "total_documents": len(chunks)
    # }
