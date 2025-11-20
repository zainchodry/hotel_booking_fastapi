from pydantic_settings import BaseSettings
import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI:str
    SECRET_KEY:str
    ALGORITHM:str


    class Config:
        env_file = ENV_PATH
        env_file_encoding = 'utf-8'

settings = Settings()
