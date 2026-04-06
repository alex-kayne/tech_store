from services.orders.repository import OrdersRepository


class OrdersService:
    def __init__(self, order_repository: OrdersRepository):
        self.order_repository = order_repository