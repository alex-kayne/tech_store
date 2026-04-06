from services import CategoryRepository
from services import CategoryService
from services import ProductsRepository
from services import ProductsService


def get_category_service() -> CategoryService:
    return CategoryService(category_repository=CategoryRepository())

def get_product_service() -> ProductsService:
    return ProductsService(products_repository=ProductsRepository())
