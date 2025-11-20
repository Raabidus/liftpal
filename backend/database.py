"""
database.py
- Asynchronous db connection
"""

"""
db zatím sync - asnyc conn mi nefungovalo v provozu ani v rámci testů
"""

from typing import AsyncGenerator
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy import engine, create_engine
from .config import DATABASE_URL

engine = create_async_engine(DATABASE_URL)

DBSession = async_sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()

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


# sync get_db
# def get_db():
#     with DBSession() as session:
#         yield session



"""
future async connection - need to test it
"""

# import asyncio

# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy import D

# async_engine = create_async_engine("postgresql+psycopg2://me@localhost/mydb") #vytvořit v configu url - url musí být taky něco v async

# AscSession = async_sessionmaker(async_engine)

# async def async_get_db():
#     async with async_engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create.all) # když bych chtěl vytvořit db
    
#     db = AscSession()
#     try:
#         yield db
#     finally:
#         await db.close

# #např. použití

# @app.post("/user")
# async def create_user (user: UserBase, db: AsyncSession = Depends(async_get_db)):
#     db_user = User(username=user.usernam)
#     db.add(db_user)
#     await db.commit()
#     await db.refresh()
#     return DBSession
