from fastapi import APIRouter, Depends

from app import const
from app.schemas.clients.api import ClientCreate
from app.schemas.common.api import ApiResponse
from app.services.clients.service import ClientsService
from app.dependencies import get_clients_service
router = APIRouter(prefix=const.API_PREFIX)

@router.post("/create_order", tags=["orders"])
async def create_client(data: ClientCreate,
                        client_service: ClientsService = Depends(get_clients_service)) -> ApiResponse:
    new_id = await client_service.create_client(data)
    return ApiResponse(success=True, message=f"Client created {new_id=}")
