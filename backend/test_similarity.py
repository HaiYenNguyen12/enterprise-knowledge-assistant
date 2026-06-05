from sklearn.metrics.pairwise import cosine_similarity
from app.services.embedding_service import get_embeddings

text1 = "Annual vacation policy"
text2 = "Employee leave rules"
text3 = "Football World Cup"
text4 = "Machine learning algorithms"

embedding1 = get_embeddings(text1)
embedding2 = get_embeddings(text2)
embedding3 = get_embeddings(text3)
embedding4 = get_embeddings(text4)

similarity_1_2 = cosine_similarity([embedding1], [embedding2])[0][0]
similarity_1_3 = cosine_similarity([embedding1], [embedding3])[0][0]
similarity_1_4 = cosine_similarity([embedding1], [embedding4])[0][0]
print(f"Similarity between '{text1}' and '{text2}': {similarity_1_2:.4f}")
print(f"Similarity between '{text1}' and '{text3}': {similarity_1_3:.4f}")
print(f"Similarity between '{text1}' and '{text4}': {similarity_1_4:.4f}")