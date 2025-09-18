

from sqlalchemy.orm import Session

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
def create_user(db: Session, data: schemas.UserCreate):
    user_instance = models.User(**data.model_dump())
    db.add(user_instance)
    db.commit()
    db.refresh
    return user_instance

#OK
def get_trainings(db: Session) -> list:
    return db.query(models.Training).all()

#OK
def get_training(db: Session, id: int):
    return db.query(models.Training).filter(models.Training.training_id==id).first()

#OK
def create_training(db: Session, data: schemas.TrainingCreateForUser):
    training_instance = models.Training(**data.model_dump()) #.model.dump() vrací Pydantic model jako dict
    db.add(training_instance)
    db.commit()
    db.refresh
    return training_instance
# vymyslet jak udělat u optional polí (type, note) když se nevyplnít = None
# aktuálně to v db vytváří [null]

#OK
def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.user_id==id).first()

#OK
def create_exercise(db: Session, data: schemas.ExerciseBase):
    exercise_instance = models.Exercise(**data.model_dump())
    db.add(exercise_instance)
    db.commit()
    db.refresh
    return exercise_instance
# přidat něco, aby v případě, že se nevyplní descriptiona a type - doplní se string něco

def get_exercises(db: Session) -> list:
    return db.query(models.Exercise).all()

def get_exercise(db: Session, id: int):
    return db.query(models.Exercise).filter(models.Exercise.exercise_id==id).first()

# nejsem si jistý jestli bude fungovat - respektive nevím jak to uděůat
def add_exercise_to_trainings(
        db: Session,
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




