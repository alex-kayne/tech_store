from services.categories.service import CategoryService
from .services.categories.repository import CategoryRepository


def get_category_service():
    return CategoryService(category_repository=CategoryRepository())
