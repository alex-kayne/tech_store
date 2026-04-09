from .repository import CategoryRepository
from app.schemas.categories import api
from app.schemas.common.api import ApiResponse

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository


    async def create_category(self, data: api.CategoryCreation) -> ApiResponse:
        if new_id := await self.category_repository.create_category(data):
            return ApiResponse(success=True, message=f"Category created {new_id=}")
        return ApiResponse(success=False, message=f"Error while creating category")
