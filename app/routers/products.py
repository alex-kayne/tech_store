from fastapi import APIRouter, Depends

from app import const
from app.schemas.products.api import ProductCreate
from app.schemas.common.api import ApiResponse
from app.services import ProductsService
from app.dependencies import get_product_service
router = APIRouter(prefix=const.API_PREFIX)

@router.post("/create_product", tags=["products"])
async def create_product(data: ProductCreate,
                          product_service: ProductsService = Depends(get_product_service)) -> ApiResponse:
    new_id = await product_service.create_product(data)
    return ApiResponse(success=True, message=f"Product created {new_id=}")
