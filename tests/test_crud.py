import pytest
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from backend.database import Base
from backend.models import User, Exercise, Training, TrainingExercise
from backend.schemas import UserCreate, TrainingCreateForUser, TrainingRead, UserTrainingRead, ExerciseAddToTraining
from backend.crud import create_user
from backend.config import DATABASE_URL

pytestmark = pytest.mark.asyncio

@pytest.fixture(scope="module")
async def test_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Yield session for tests
    async with async_session() as session:
        return session

    # Cleanup
    await engine.dispose()

async def test_create_user(
        test_session: AsyncSession
    ):
    
    user_data = UserCreate(usernam="testerusername", password="pass123")
    user = UserCreate(test_session, user_data)

    assert user.username == "testerusername"
    assert user.id is not None

