from sqlite3 import Row

import app.db as sqlite_db
from app.schemas.categories import api


class CategoryRepository:

    async def create_category(self, data: api.CategoryCreation) -> int:
        sql_text = "INSERT INTO categories (name, parent_id) VALUES (?, ?) RETURNING id"
        new_id = await sqlite_db.returning_insert(sql_text, (data.name, data.parent_id))
        return new_id

    async def get_category_by(self, category_id: int) -> Row | None:
        sql_text = f"SELECT * FROM categories WHERE id = {category_id} LIMIT 1"
        return await sqlite_db.select_one_row(sql_text)
