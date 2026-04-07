from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["healthcheck"])
async def ping() -> str:
    return "pong"
