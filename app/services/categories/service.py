from .repository import CategoryRepository
from app.schemas.categories import api

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository


    async def create_category(self, data: api.CategoryCreation) -> int:
        return await self.category_repository.create_category(data)