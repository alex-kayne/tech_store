from fastapi import APIRouter, Depends

from app import const
from app.schemas.categories.api import CategoryCreation
from app.schemas.common.api import ApiResponse
from app.services.categories.service import CategoryService
from app.dependencies import get_category_service
router = APIRouter(prefix=const.API_PREFIX)

@router.post("/create_category")
async def create_category(data: CategoryCreation,
                          category_service: CategoryService = Depends(get_category_service)) -> ApiResponse:
    new_id = await category_service.create_category(data)
    return ApiResponse(success=True, message=f"Category created {new_id=}")
