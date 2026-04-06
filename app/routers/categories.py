from fastapi import APIRouter

from app import const
from app.schemas.categories.api import CategoryCreation
from app.schemas.common.api import ApiResponse

router = APIRouter(prefix=const.API_PREFIX)

@router.post("/create_category")
async def create_category(data: CategoryCreation) -> ApiResponse:
    return ApiResponse(success=True, message="Category created")
