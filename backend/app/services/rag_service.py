from backend.app.services.embedding_service import get_embeddings
from backend.app.services.llm_service import generate_response
from backend.app.core.qdrant_client import client

def answer_question(question: str):
  collection_info = client.get_collection(collection_name="knowledge_base")
  if collection_info.points_count == 0:
        return "No documents have been uploaded yet. Please upload a document to ask questions about its content."
    # 1. Extract text from PDF
    # pdf_path = "uploads/OutSystems Engineer.pdf"
    # text = extract_text_from_pdf(pdf_path)

    # 2. Split text into chunks
    # chunks = split_text_into_chunks(text, chunk_size=500, chunk_overlap=100)

    # 3. Get embedding for the question
  query_embedding = get_embeddings(question)

  # 4. Calculate similarity scores for each chunk
  # chunk_embeddings  = []
  # for chunk in chunks:
  #     chunk_embedding = get_embeddings(chunk)
  #     score = cosine_similarity([chunk_embedding], [query_embedding])[0][0]
  #     chunk_embeddings.append(
  #         {
  #           "chunk": chunk,
  #           "embedding": chunk_embedding,
  #           "similarity_score": score
  #         })
  
  # 5. Sort chunks by similarity score and select top 3
  # sorted_chunks = sorted(collection_info.points, key=lambda x: cosine_similarity([x["vector"]], [query_embedding])[0][0], reverse=True)
  # top_chunks = sorted_chunks[:3]

  results = client.query_points(
    collection_name="knowledge_base",
    query=query_embedding.tolist(),
    limit=3
  )
  print(results)
  print(type(results))
  # 6. Create context and prompt for LLM
  context = "\n\n".join([point.payload["chunk"] for point in results.points])
  prompt = f"""
  You are a helpful assistant.

  Answer the question ONLY based on the provided context.

  If the answer cannot be found in the context,
  say:

  'I cannot find the answer in the provided document.'

  Context:
  {context}

  Question:
  {question}

  Answer:
  """
  
  # 7. Generate response from LLM
  response = generate_response(prompt)
  
  return response