from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import setting

DATABASE_URL = f"postgresql+asyncpg://{setting.DB_USER}:{setting.DB_PASS}@{setting.DB_HOST}:{setting.DB_PORT}/{setting.DB_NAME}"

engine = create_async_engine(DATABASE_URL)

async_session_maker = sessionmaker(bind=engine, class_= AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass