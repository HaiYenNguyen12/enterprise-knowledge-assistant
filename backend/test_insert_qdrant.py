from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from app.services.embedding_service import get_embeddings

client = QdrantClient(host="localhost", port=6333)
# Example document chunk
text_chunk = "Employees are entitled to 14 annual leave days per year."

embedding = get_embeddings(text_chunk)
client.upsert(
  collection_name="knowledge_base",
  points=[
    PointStruct(
      id=1,
      vector=embedding,
      payload={"chunk": text_chunk}
    )
  ]
)
print("Document chunk inserted into Qdrant successfully.")