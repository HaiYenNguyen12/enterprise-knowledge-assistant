from qdrant_client import QdrantClient,models
from backend.app.core.settings import settings

class QdrantRepository:
    def __init__(self, client):
        self.client = client


    def get_collection (self):
       return self.client.get_collection(collection_name=settings.collection_name)


    def upsert_chunks(self, points):
        self.client.upsert(
            collection_name=settings.collection_name,
            points=points
        )
    
    def search_chunks(self, query_vector,document_ids = None, limit=3):
        if document_ids:
            query_filter = models.Filter(
                must=[
                    models.FieldCondition(
                        key="document_id",
                        match=models.MatchAny(any=document_ids)
                    )
                ]
                
            )
        else:
            query_filter = None

        return self.client.query_points(
            collection_name=settings.collection_name,
            query_filter = query_filter,
            query=query_vector,
            limit=limit
        )
    
    def delete_chunks_by_document_id(self,document_id):
        self.client.delete(
            collection_name=settings.collection_name,
            points_selector=models.FilterSelector(
                filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="document_id",
                            match=models.MatchValue(value=document_id)
                        )
                    ]
                )
            )
        )