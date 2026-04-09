from fastapi import APIRouter, Depends

from app import const
from app.schemas.common.api import ApiResponse
from app.schemas.orders.api import CreateOrder, AddProduct
from app.services.orders.service import OrdersService
from app.dependencies import get_orders_service

router = APIRouter(prefix=const.API_PREFIX)


@router.post("/create_order", tags=["orders"])
async def create_order(data: CreateOrder,
                       order_service: OrdersService = Depends(get_orders_service)) -> ApiResponse:
    """
    Order creation endpoint. Booking products while the creation process is running with transactions to prevent race conditions
    """
    result = await order_service.create_order(data)
    return result


@router.post("/add_product", tags=["orders"])
async def add_product(data: AddProduct,
                      order_service: OrdersService = Depends(get_orders_service)) -> ApiResponse:
    """
    Product adding endpoint. Booking products while the adding process is running with transactions to prevent race conditions
    """
    result = await order_service.add_product_to_order(data)
    return result
