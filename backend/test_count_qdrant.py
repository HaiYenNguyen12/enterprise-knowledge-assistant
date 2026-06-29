from app.core.qdrant_client import client
from app.core.settings import settings

# print(client.get_collections())
info = client.get_collection(collection_name=settings.collection_name)
print(info.points_count)