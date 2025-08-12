

from sqlalchemy.orm import Session

from . import models
from . import schemas


#TODO
#db operace

# add training to user
# copy trainng from users trainng
# add exercise to trainng
# delete
# confirm function



# async def create_user(
#     db: AsyncSession,
#     user: UserCreate
#     ) -> User:

#     new_user = User(**user.dict())
#     db.add(new_user)
#     await db.commit
#     await db.refresh(new_user)
#     return new_user

def create_user(db: Session, data: schemas.UserCreate):
    user_instance = models.User(**data.model_dump())
    db.add(user_instance)
    db.commit()
    db.refresh
    return user_instance

def get_all_trainings(db: Session):
    return db.query(models.Training).all()

def create_training(db: Session, data: schemas.TrainingCreateForUser):
    training_instance = models.Training(**data.model_dump())
    db.add(training_instance)
    db.commit()
    db.refresh
    return training_instance


def create_exercise():
    pass

def add_exercise_to_training():
    pass




