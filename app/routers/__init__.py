from .categories import router as categories_router
from .products import router as products_router
from .clients import router as clients_router

ALL_ROUTERS = (categories_router, products_router, clients_router,)
