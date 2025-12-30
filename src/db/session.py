from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import Settings


DATABASE_URL = f"postgresql+asyncpg://{Settings().db_user}:{Settings().db_password}@{Settings().db_host}:{Settings().db_port}/{Settings().db_name}"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with SessionLocal() as session:
        yield session