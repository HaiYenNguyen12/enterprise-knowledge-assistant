class QdrantRepository:
    def __init__(self, client):
        self.client = client

    def upsert_chunks(self, points):
        self.client.upsert(
            collection_name="knowledge_base",
            points=points
        )
    
    def search_chunks(self, query_vector, limit=3):
        return self.client.query_points(
            collection_name="knowledge_base",
            query_vector=query_vector,
            limit=limit
        )