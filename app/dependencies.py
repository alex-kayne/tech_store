from app.services.categories.repository import CategoryRepository
from app.services.categories.service import CategoryService
from app.services.clients.repository import ClientsRepository
from app.services.clients.service import ClientsService
from app.services.common.repository import CategoryProductQueryRepository
from app.services.products.repository import ProductsRepository
from app.services.products.service import ProductsService
from app.services.orders.service import OrdersService
from app.services.orders.repository import OrdersRepository

def get_category_service() -> CategoryService:
    return CategoryService(category_repository=CategoryRepository())

def get_product_service() -> ProductsService:
    return ProductsService(products_repository=ProductsRepository(),
                           category_repository=CategoryRepository(),
                           category_product_repository=CategoryProductQueryRepository())

def get_clients_service() -> ClientsService:
    return ClientsService(clients_repository=ClientsRepository())

def get_orders_service() -> OrdersService:
    return OrdersService(order_repository=OrdersRepository())
