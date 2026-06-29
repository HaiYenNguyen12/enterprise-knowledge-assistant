from sentence_transformers import SentenceTransformer
from backend.app.core.settings import settings
model = SentenceTransformer(settings.embedding_model)

def get_embeddings(text: str):
    return model.encode(text)