from services.categories.repository import CategoryRepository
from services.categories.service import CategoryService
from services.clients.repository import ClientsRepository
from services.clients.service import ClientsService
from services.common.repository import CategoryProductQueryRepository
from services.products.repository import ProductsRepository
from services.products.service import ProductsService
from services.orders.service import OrdersService
from services.orders.repository import OrdersRepository

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
