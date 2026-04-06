from schemas.products.api import ProductCreate
from .repository import ProductsRepository
class ProductsService:
    def __init__(self, products_repository: ProductsRepository):
        self.products_repository = products_repository

    async def create_product(self, data: ProductCreate) -> int:

        new_product_id = await self.products_repository.create_product(data)
        await self.products_repository.create_product_category_link(new_product_id, data.category_id)
        return new_product_id
