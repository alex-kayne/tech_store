from collections.abc import Collection

import app.db as sqlite_db


class OrdersRepository:

    async def is_products_exists_and_available(self, products_ids: Collection[str]) -> bool:
        sql_text = f"""SELECT count(*) FROM products WHERE id in (", ".join(products_ids)) and quantity > 0"""
        return len(products_ids) == (await sqlite_db.select_one_row(sql_text))[0]

    async def create_order(self, products_ids: Collection[str]) -> bool:
        sql_text = f"""
                    UPDATE products
                    SET 
                    """