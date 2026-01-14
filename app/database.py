from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import setting

if setting.MODE == "TEST":
    DATABASE_URL = f"postgresql+asyncpg://{setting.TEST_DB_USER}:{setting.TEST_DB_PASS}@{setting.TEST_DB_HOST}:{setting.TEST_DB_PORT}/{setting.TEST_DB_NAME}"
    DATABASE_PARAMS = {"poolclass" : NullPool}
else:
    DATABASE_URL = f"postgresql+asyncpg://{setting.DB_USER}:{setting.DB_PASS}@{setting.DB_HOST}:{setting.DB_PORT}/{setting.DB_NAME}"
    DATABASE_PARAMS = {}


    


engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

async_session_maker = sessionmaker(bind=engine, class_= AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass