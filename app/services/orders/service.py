from app.schemas.common.api import ApiResponse
from app.schemas.orders.api import CreateOrder, AddProduct
from app.services.orders.repository import OrdersRepository


class OrdersService:
    def __init__(self, order_repository: OrdersRepository):
        self.order_repository = order_repository

    async def create_order(self, data: CreateOrder) -> ApiResponse:
        if not await self.order_repository.is_products_exists_and_available([str(product.product_id) for product in data.products]):
            return ApiResponse(success=False, message="Some of the products is not available")

        if new_order_id := await self.order_repository.create_order(data):
            return ApiResponse(success=True, message=f"Order created successfully {new_order_id=}")

        return ApiResponse(success=False, message="Could not create order")


    async def add_product_to_order(self, data: AddProduct) -> ApiResponse:
        if not await self.order_repository.is_order_exists(data.order_id):
            return ApiResponse(success=False, message="Order doesn`t exist")


        if not await self.order_repository.is_products_exists_and_available([str(data.product_id)]):
            return ApiResponse(success=False, message="Product is not available")

        if await self.order_repository.add_product_to_order(data):
            return ApiResponse(success=True, message="Product added to order")
        return ApiResponse(success=False, message="Couldn`t add product to order")
