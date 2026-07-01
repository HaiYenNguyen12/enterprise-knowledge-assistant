from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str
    document_ids: list[str] | None = None

class QuestionResponse(BaseModel):
    pass