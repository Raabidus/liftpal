

from sqlalchemy.orm import Session

from . import models
from . import schemas


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
def get_trainings(db: Session):
    return db.query(models.Training).all()

#OK
def get_training(db: Session, id:int):
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
def get_user(db: Session, id:int):
    return db.query(models.User).filter(models.User.user_id==id).first()

def create_exercise():
    pass

def add_exercise_to_training():
    pass




