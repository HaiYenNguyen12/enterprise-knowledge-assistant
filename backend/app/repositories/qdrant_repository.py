
class QdrantRepository:
    def __init__(self, client):
        self.client = client


    def get_collection (self):
       return self.client.get_collection(collection_name="knowledge_base")


    def upsert_chunks(self, points):
        self.client.upsert(
            collection_name="knowledge_base",
            points=points
        )
    
    def search_chunks(self, query_vector,document_ids = None, limit=3):
        return self.client.query_points(
            collection_name="knowledge_base",
            query=query_vector,
            limit=limit
        )