from fastapi import APIRouter, UploadFile, File
from pathlib import Path


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

router = APIRouter(prefix="/documents", tags=["documents"])

@router.get("/")
def get_document():
    return {"message": "Document API is working!"}

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_location = UPLOAD_DIR / file.filename
    with open(file_location, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
        
    return {
        "filename": file.filename,
        "file_location": str(file_location)
    }
