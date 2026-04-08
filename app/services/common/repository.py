from aiosqlite import Row
from collections.abc import Iterable

import app.db as sqlite_db


class CategoryProductQueryRepository:

    async def get_categories_with_products(self) -> Iterable[Row]:
        sql_text = """SELECT *
                      FROM 
                      (SELECT c.name, c.parent_id, parent_c.name as parent_name, NULL as price, NULL as quantity
                      FROM categories AS c 
                      LEFT JOIN categories AS parent_c ON c.parent_id = parent_c.id
                      
                      UNION 
                      
                      SELECT p.name, chp.category_id, c.name, p.price, p.quantity
                      FROM products AS p
                      JOIN categories_has_products AS chp ON chp.product_id = p.id
                      JOIN categories AS c ON chp.category_id = c.id)
                      ORDER BY parent_id ASC NULLS FIRST"""
        categories_with_products = await sqlite_db.select(sql_text)
        return categories_with_products
