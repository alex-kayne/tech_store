from fastapi import APIRouter, Depends

from app import const
from app.schemas.products.api import ProductCreate
from app.schemas.common.api import ApiResponse
from app.services.products.service import ProductsService
from app.dependencies import get_product_service

router = APIRouter(prefix=const.API_PREFIX)

@router.post("/create_product", tags=["products"])
async def create_product(data: ProductCreate,
                          product_service: ProductsService = Depends(get_product_service)) -> ApiResponse:
    """
    Product creation endpoint
    """
    new_id = await product_service.create_product(data)
    if new_id:
        return ApiResponse(success=True, message=f"Product created {new_id=}")
    else:
        return ApiResponse(success=False, message="Product creation failed. No such category")

@router.get("/product_tree", tags=["products"])
async def get_product_tree(product_service: ProductsService = Depends(get_product_service)) -> ApiResponse:
    """
    Visualize categories and products like a tree in JSON format
    """
    product_tree = await product_service.get_product_tree()
    return ApiResponse(success=True, data=product_tree)
