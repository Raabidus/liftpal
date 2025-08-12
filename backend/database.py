"""
database.py
- Asynchronous db connection
"""

"""
db zatím sync - asnyc conn mi nefungovalo v provozu ani v rámci testů
"""

# from typing import AsyncGenerator
from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import engine, create_engine
from .config import DATABASE_URL


#TODO



engine = create_engine(DATABASE_URL)

# async_engine = create_async_engine(DATABASE_URL, echo=True)
DBSession = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()



# DBSession = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


def get_db():
    with DBSession() as session:
        yield session


