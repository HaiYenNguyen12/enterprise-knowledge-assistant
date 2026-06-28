from fastapi import Request
from fastapi.responses import JSONResponse
from backend.app.exceptions.document_exception import DocumentNotFoundException

def document_not_found_exception_handler(request: Request, exc: DocumentNotFoundException):
  return JSONResponse(
    status_code=404,
    content={
      "success" : False,
      "error": {
        "code": "DOCUMENT_NOT_FOUND",
        "message":str(exc)
      }
    } 
  )