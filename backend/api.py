

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session

from backend import models
from backend import schemas
from backend import crud
from backend import database


app = FastAPI()



#TODO

# get all users training - select by user_id
# create exercise
# add exercise to training

#OK
@app.post("/users/", response_model=schemas.UserCreate)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)
# vytvořit if statement, kdyby username už existovalo
# bude se muset upravit model/schema, nebo oboje?

#OK
@app.get("/users/{id}", response_model=schemas.UserBase)
def get_user_by_id(id: int, db: Session = Depends(database.get_db)):
    user_query = crud.get_user(db, id)
    if user_query:
        return user_query
    raise HTTPException(status_code=404, detail="Blbý ID uživatele")

#OK
@app.get("/trainings/", response_model= list[schemas.TrainingRead])
def get_all_trainings(db: Session = Depends(database.get_db)):
    return crud.get_trainings(db)

#OK
@app.get("/trainings/{id}", response_model = schemas.TrainingRead)
def get_training_by_id(id:int, db:Session = Depends(database.get_db)):
    training_query = crud.get_training(db, id)
    if training_query:
        return training_query
    raise HTTPException(status_code=404, detail='Blbý ID tréningu')

#OK
@app.post("/trainings/", response_model=schemas.TrainingCreateForUser)
def create_new_training(training: schemas.TrainingCreateForUser, db: Session = Depends(database.get_db)):
    return crud.create_training(db, training)

#OK
@app.post("/exercises/", response_model=schemas.ExerciseCreate)
def create_new_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(database.get_db)):
    return crud.create_exercise(db, exercise)


@app.get("/exercises/{id}", response_model = schemas.ExerciseRead)
def get_exercise_by_id(id: int, db: Session = Depends(database.get_db)):
    exercise_query = crud.get_exercise(db, id)
    if exercise_query:
        return exercise_query
    raise HTTPException(status_code=404, detail='Blbý ID cviku')

@app.get("/exercises/", response_model= list[schemas.ExerciseRead])
def get_all_exercises(db: Session = Depends(database.get_db)):
    return crud.get_exercises(db)
#když se nevyplní type, description je Null a není string, v tu chvíli nefungije get