from schemas.common.api import ApiResponse
from schemas.orders.api import CreateOrder
from services.orders.repository import OrdersRepository


class OrdersService:
    def __init__(self, order_repository: OrdersRepository):
        self.order_repository = order_repository

    async def create_order(self, data: CreateOrder) -> ApiResponse:
        if not await self.order_repository.is_products_exists_and_available([str(product.product_id) for product in data.products]):
            return ApiResponse(success=False, message="Some of the products is not available")

        

        return ApiResponse