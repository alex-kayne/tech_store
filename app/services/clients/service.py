from app.schemas.clients.api import ClientCreate
from .repository import ClientsRepository
from app.schemas.common.api import ApiResponse

class ClientsService:
    def __init__(self, clients_repository: ClientsRepository):
        self.clients_repository = clients_repository

    async def create_client(self, data: ClientCreate) -> ApiResponse:
        if new_id := await self.clients_repository.create_client(data):
            return ApiResponse(success=True, message=f"Client created {new_id=}")
        return ApiResponse(success=False, message=f"Error creating client")
