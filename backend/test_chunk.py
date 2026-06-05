from app.services.chunk_service import split_text_into_chunks
from app.services.pdf_service import extract_text_from_pdf

pdf_path = "uploads\OutSystems Engineer.pdf"
text = extract_text_from_pdf(pdf_path)
chunks = split_text_into_chunks(text)

print(f"Total chunks created: {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n{'-'*40}")