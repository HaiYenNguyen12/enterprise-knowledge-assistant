from app.services.pdf_service import extract_text_from_pdf

test = extract_text_from_pdf("uploads/OutSystems Engineer.pdf")
print(test)