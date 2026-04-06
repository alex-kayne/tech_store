from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    address: str
