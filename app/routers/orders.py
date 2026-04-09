from fastapi import APIRouter, Depends

from app import const
from app.schemas.common.api import ApiResponse
from app.schemas.orders.api import CreateOrder
from app.services.orders.service import OrdersService
from dependencies import get_orders_service

router = APIRouter(prefix=const.API_PREFIX)


@router.post("/create_order", tags=["orders"])
async def create_order(data: CreateOrder,
                       order_service: OrdersService = Depends(get_orders_service)) -> ApiResponse:
    result = await order_service.create_order(data)
    return result
