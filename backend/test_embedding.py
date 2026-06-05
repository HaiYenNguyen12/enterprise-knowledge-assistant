from app.services.embedding_service import get_embeddings

text = """Employees are entitled to 14 annual leave days per year."""
embeddings = get_embeddings(text)
print(f"Embeddings for the text:\n{text}\n")
print(embeddings)
print(len(embeddings))
print(type(embeddings))