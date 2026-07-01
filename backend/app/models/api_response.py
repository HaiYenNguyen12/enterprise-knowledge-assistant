from pydantic import BaseModel
from typing import Any


class ApiResponse(BaseModel):
    status: bool
    message: str | None = None
    data: Any = None