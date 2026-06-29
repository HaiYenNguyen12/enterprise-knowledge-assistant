from qdrant_client import QdrantClient
from app.core.settings import settings
from app.services.embedding_service import get_embeddings

client = QdrantClient(host="localhost", port=6333)
query = "How many annual leave days do employees get?"
query_embedding = get_embeddings(query)

results = client.query_points(
    collection_name=settings.collection_name,
    query= query_embedding.tolist(),
    limit=3 # Get top 3 most similar chunks
)

print(results)