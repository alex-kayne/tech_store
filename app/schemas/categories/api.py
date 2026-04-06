from pydantic import BaseModel


class CategoryCreation(BaseModel):
    name: str
    parent_id: int | None
