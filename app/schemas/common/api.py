from pydantic import BaseModel

class ApiResponse(BaseModel):
    success: bool
    message: str | None = None
    data: dict | None = None
