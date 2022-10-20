import os

from dotenv import load_dotenv
from pathlib import Path


env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = 'LinkShortener'
    PROJECT_VERSION: str = '1.0.0'

    POSTGRES_USER: str = os.getenv('DB_USER', 'postgres')
    POSTGRES_PASSWORD: str = os.getenv('DB_PASSWORD', 'postgres')
    POSTGRES_SERVER: str = os.getenv('DB_HOST', 'db')
    POSTGRES_PORT: str = os.getenv('DB_PORT', 5432)
    POSTGRES_DB: str = os.getenv('DB_NAME', 'postgres')
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'
    DOMAIN_NAME: str = '127.0.0.1:8000'


settings = Settings()
