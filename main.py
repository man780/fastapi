from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from settings import settings

from routers import system, refs, vk

app = FastAPI(
    title=settings.app_name,
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(DBSessionMiddleware, db_url=settings.database_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(system.router)
app.include_router(refs.router)
app.include_router(vk.router)
