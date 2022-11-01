from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from settings import settings

from routers import liveness

load_dotenv(".env")

app = FastAPI(
    title=settings.app_name,
)

app.add_middleware(DBSessionMiddleware, db_url=settings.database_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(liveness.router)


# @app.get("/health_check")
# async def root():
#     return {"success": True}
