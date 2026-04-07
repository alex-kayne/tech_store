from sqlite3 import Row
from typing import Iterable, Dict, Tuple

from app.services.common.repository import CategoryProductQueryRepository
from app.services.categories.repository import CategoryRepository
from schemas.products.api import ProductCreate
from .repository import ProductsRepository


class ProductsService:
    def __init__(self, products_repository: ProductsRepository,
                 category_repository: CategoryRepository,
                 category_product_repository: CategoryProductQueryRepository):
        self.category_repository = category_repository
        self.category_product_repository = category_product_repository
        self.products_repository = products_repository

    async def create_product(self, data: ProductCreate) -> int | None:
        if not await self.category_repository.get_category_by(data.category_id):
            return
        new_product_id = await self.products_repository.create_product(data)
        await self.products_repository.create_product_category_link(new_product_id, data.category_id)
        return new_product_id

    def _build_product_tree(self, categories_with_products: Iterable[Row]) -> dict:
        path_dict: Dict[str, Tuple] = {}
        product_tree = {}
        for rec in categories_with_products:
            name = rec[0]
            parent_name = rec[2]
            price = rec[3]
            quantity = rec[4]

            if path := path_dict.get(parent_name):
                path_dict[name] = (*path, name)
                linked_obj = None
                for key in path:
                    if linked_obj is None:
                        linked_obj = product_tree[key]
                    else:
                        linked_obj = linked_obj[key]
                if not price:
                    linked_obj[name] = {}
                else:
                    linked_obj[name] = {"price": price, "quantity": quantity,}
            else:
                path_dict[name] = (name, )
                product_tree[name] = {}

        return product_tree

    async def get_product_tree(self) -> dict:

        categories_with_products = await self.category_product_repository.get_categories_with_products()

        return self._build_product_tree(categories_with_products)
