from app.services.chunk_service import split_text_into_chunks
from app.services.pdf_service import extract_text_from_pdf
from sklearn.metrics.pairwise import cosine_similarity
from app.services.embedding_service import get_embeddings
from app.services.llm_service import generate_response

pdf_path = "uploads/OutSystems Engineer.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text, chunk_size=500, chunk_overlap=100)

query = input("Ask a question related to the document: ")
query_embedding = get_embeddings(query)
print(f"Total chunks created: {len(chunks)}")

chunk_embeddings  = []
for chunk in chunks:
    chunk_embedding = get_embeddings(chunk)
    score = cosine_similarity([chunk_embedding], [query_embedding])[0][0]
    chunk_embeddings.append(
        {
          "chunk": chunk,
          "embedding": chunk_embedding,
          "similarity_score": score
        })

sorted_chunks = sorted(chunk_embeddings, key=lambda x: x["similarity_score"], reverse=True)
top_chunks = sorted_chunks[:3]
context = "\n\n".join([chunk["chunk"] for chunk in top_chunks])
prompt = f"""
You are a helpful assistant.

Answer the question ONLY based on the provided context.

If the answer cannot be found in the context,
say:

'I cannot find the answer in the provided document.'

Context:
{context}

Question:
{query}

Answer:
"""
print(prompt)

response = generate_response(prompt)
print("Response from LLM:")
print(response)
# print("Chunks sorted by similarity to the query:")
# for i in range(3):
#   chunk_info = sorted_chunks[i]
#   print(f"Chunk {i+1}:\n{chunk_info['chunk']}\nSimilarity: {chunk_info['similarity_score']:.4f}\n{'-'*40}")