from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from app.services.embedding_service import get_embeddings
from app.core.settings import settings

client = QdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)
# Example document chunk
text_chunk = "Employees are entitled to 14 annual leave days per year."

embedding = get_embeddings(text_chunk)
client.upsert(
  collection_name=settings.collection_name,
  points=[
    PointStruct(
      id=1,
      vector=embedding,
      payload={"chunk": text_chunk}
    )
  ]
)
print("Document chunk inserted into Qdrant successfully.")