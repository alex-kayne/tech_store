import app.db as sqlite_db
from schemas.products.api import ProductCreate

class ProductsRepository:

    async def create_product(self, data: ProductCreate) -> int:
        sql_text = "INSERT INTO products (name, quantity, price) VALUES (?, ?, ?) RETURNING id"
        new_id = await sqlite_db.returning_insert(sql_text, (data.name, data.quantity, data.price))
        return new_id

    async def create_product_category_link(self, product_id: int, category_id: int) -> None:
        sql_text = "INSERT INTO categories_has_products (product_id, category_id) VALUES (?, ?)"
        await sqlite_db.insert(sql_text, (product_id, category_id,))
