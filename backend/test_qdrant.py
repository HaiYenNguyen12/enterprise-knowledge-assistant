from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from app.core.settings import settings

client = QdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)
print(client.get_collections())

client.create_collection(
    collection_name=settings.collection_name,
    vectors_config=VectorParams(size=settings.embedding_dimension, distance=Distance.COSINE)
)

print(f"Collection {settings.collection_name} created successfully.")
