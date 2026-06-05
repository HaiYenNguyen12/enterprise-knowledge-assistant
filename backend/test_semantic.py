from app.services.chunk_service import split_text_into_chunks
from app.services.pdf_service import extract_text_from_pdf
from sklearn.metrics.pairwise import cosine_similarity
from app.services.embedding_service import get_embeddings

pdf_path = "uploads\OutSystems Engineer.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text, chunk_size=500, chunk_overlap=100)

query = input("Ask a question related to the document: ")

print(f"Total chunks created: {len(chunks)}")

embedding = get_embeddings(query)

chunk_embeddings  = []
for chunk in chunks:
    chunk_embeddings.append(
        {
          "chunk": chunk,
          "embedding": get_embeddings(chunk)
        })
query_embedding = get_embeddings(query)
sorted_chunks = sorted(chunk_embeddings, key=lambda x: cosine_similarity([x["embedding"]],[query_embedding])[0][0], reverse=True)
print("Chunks sorted by similarity to the query:")
for i in range(3):
  chunk_infor = sorted_chunks[i]
  print(f"Chunk {i+1}:\n{chunk_infor['chunk']}\nSimilarity: {cosine_similarity([chunk_infor['embedding']], [query_embedding])[0][0]:.4f}\n{'-'*40}")