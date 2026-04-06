from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from loguru import logger
from app.routers import ALL_ROUTERS
from app.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # init db
    await init_db()
    logger.info("Sqlite DB init - success")
    for router in ALL_ROUTERS:
        app.include_router(router)
    logger.info("Routers including - success")
    yield


app = FastAPI(lifespan=lifespan)

if __name__ == '__main__':
    uvicorn.run("main:app")
