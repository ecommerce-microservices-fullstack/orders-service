from pydantic import Field
from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    kafka_bootstrap: str = Field(os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092"))

    db_user: str = Field(os.getenv("POSTGRES_USER"))
    db_password: str = Field(os.getenv("POSTGRES_PASSWORD"))
    db_name: str = Field(os.getenv("POSTGRES_DB"))
    db_host: str = Field(os.getenv("POSTGRES_HOST"))
    db_port: str = Field(os.getenv("POSTGRES_PORT"))
