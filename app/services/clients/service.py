from app.schemas.clients.api import ClientCreate
from .repository import ClientsRepository


class ClientsService:
    def __init__(self, clients_repository: ClientsRepository):
        self.clients_repository = clients_repository

    async def create_client(self, data: ClientCreate) -> int:
        new_client_id = await self.clients_repository.create_client(data)
        return new_client_id
