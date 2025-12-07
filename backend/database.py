"""
database.py
- Asynchronous db connection
"""

"""
db zatím sync - asnyc conn mi nefungovalo v provozu ani v rámci testů
"""

from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from .config import DATABASE_URL

engine = create_async_engine(DATABASE_URL)

DBSession = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    FastAPI dependency yielding a db session. The session is committed if no exception occurs, otherwise it is rolled
    back.
    """
    async with DBSession() as db:
        try:
            yield db
            await db.commit()
        except Exception:
            await db.rollback()
            raise
