from app.core.qdrant_client import client
# print(client.get_collections())
info = client.get_collection(collection_name="knowledge_base")
print(info.points_count)