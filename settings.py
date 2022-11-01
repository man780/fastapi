import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv(".env")


class Settings(BaseSettings):
    app_name: str = "Pet FastAPI Project"
    database_url: str = os.environ["DATABASE_URL"]


settings = Settings()
