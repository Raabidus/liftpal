

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session

from backend import models
from backend import schemas
from backend import crud
from backend import database





#TODO

# api requesty


app = FastAPI()

@app.post("/users/", response_model=schemas.UserCreate)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)




@app.get("/trainings/", response_model=list[schemas.TrainingBase])
async def get_trainings(db: Session = Depends(database.get_db)):
    return crud.get_all_trainings(db)

@app.post("/trainings/", response_model=schemas.TrainingCreateForUser)
def create_new_training(training: schemas.TrainingCreateForUser, db: Session = Depends(database.get_db)):
    return crud.create_training(db, training)
