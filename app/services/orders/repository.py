from collections.abc import Collection
from schemas.orders.api import CreateOrder, AddProduct
import app.db as sqlite_db

class OrdersRepository:

    async def is_products_exists_and_available(self, products_ids: Collection[str]) -> bool:
        sql_text = f"""SELECT count(*) FROM products WHERE id in ({", ".join(products_ids)}) and quantity > 0"""
        return len(products_ids) == (await sqlite_db.select_one_row(sql_text))[0]

    async def is_order_exists(self, order_id: int) -> bool:
        sql_text = f"""SELECT 1 FROM orders WHERE id = {order_id} LIMIT 1;"""
        return  bool(await sqlite_db.select_one_row(sql_text))

    async def create_order(self, order_data: CreateOrder) -> int | None:
        return await sqlite_db.create_order(order_data)

    async def add_product_to_order(self, data: AddProduct) -> bool:
        return await sqlite_db.add_product_to_order(data)
