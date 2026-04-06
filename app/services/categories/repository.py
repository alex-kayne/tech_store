import app.db as sqlite_db
from app.schemas.categories import api

class CategoryRepository:
    db = sqlite_db

    async def create_category(self, data: api.CategoryCreation) -> int:
        sql_text = "INSERT INTO categories (name, parent_id) VALUES (?, ?) RETURNING id"
        new_id = await self.db.returning_insert(sql_text, (data.name, data.parent_id))
        return new_id
