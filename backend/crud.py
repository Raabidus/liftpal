

from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from . import models
from . import schemas
from . import models


#TODO
#db operace

# get all users training - select by user_id
# create exercise
# post exercise to training



# async def create_user(
#     db: AsyncSession,
#     user: UserCreate
#     ) -> User:

#     new_user = User(**user.dict())
#     db.add(new_user)
#     await db.commit
#     await db.refresh(new_user)
#     return new_user

#OK
async def create_user(db: AsyncSession,
                      data: schemas.UserCreate
                      ):
    user_instance = models.User(**data.model_dump())
    db.add(user_instance)
    await db.commit()
    await db.refresh(user_instance)
    return user_instance

# all trainings prob usless
# async def get_trainings(db: AsyncSession)-> list[models.Training]:
#     stmt = (
#         # Training returned has training.exercises already loaded → Pydantic can access it without triggering new IO.
#         select(models.Training).options(selectinload(models.Training.exercises))
#         )
#     result = await db.execute(stmt)
#     return result.scalars().all()

#OK
async def get_training(db: AsyncSession,
                       training_id: int):
    stmt = (
        select(models.Training)
        .where(models.Training.training_id == training_id)
        )
    result = await db.execute(stmt)
    training = result.scalars().first()
    return training


async def create_training(db: AsyncSession,
                          data: schemas.TrainingCreateForUser
                          ):
    training_instance = models.Training(**data.model_dump()) #.model.dump() vrací Pydantic model jako dict
    db.add(training_instance)
    await db.commit()
    await db.refresh(training_instance)
    return training_instance
# vymyslet jak udělat u optional polí (type, note) když se nevyplnít = None
# aktuálně to v db vytváří [null]

#OK
async def get_user(db: AsyncSession,
                   user_id: int
                   ):
    stmt = select(models.User).where(models.User.user_id == user_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()

#OK
async def create_exercise(db: AsyncSession,
                          data: schemas.ExerciseCreate
                          ):
    exercise_instance = models.Exercise(**data.model_dump())
    db.add(exercise_instance)
    await db.commit()
    await db.refresh(exercise_instance)
    return exercise_instance
# přidat něco, aby v případě, že se nevyplní descriptiona a type - doplní se string něco

async def get_exercises(db: AsyncSession):
    stmt = select(models.Exercise)
    result = await db.execute(stmt)
    return result.scalars().all()

async def get_exercise(db: AsyncSession,
                       exercise_id: int
                       ):
    stmt = (
        select(models.Exercise)
        .where(models.Exercise.exercise_id == exercise_id)
        )
    result = await db.execute(stmt)
    exercise = result.scalar_one_or_none()
    return exercise

# musí se upravit
def add_exercise_to_trainings(
        db: AsyncSession,
        training_id,
        exercise_id,
        data: schemas.TrainingExerciseBase
    ):
    
    new_training_exercise = models.TrainingExercise(**data.model_dump())
    db.query(models.TrainingExercise).filter_by(training_id=training_id, exercise_id=exercise_id).first()
    db.add(new_training_exercise)
    db.commit()
    db.refresh(new_training_exercise)
    return new_training_exercise