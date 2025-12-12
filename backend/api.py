

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from fastapi.routing import APIRoute


from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from backend import models
from backend import schemas
from backend import crud
from backend import database
from backend.config import settings


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# conection with frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

#TODO

# get all users training - select by user_id
# create exercise
# add exercise to training

#funguje, ale dodělat
@app.post("/users/", response_model=schemas.UserCreate, status_code=201)
async def create_new_user(user: schemas.UserCreate,
                          db: AsyncSession = Depends(database.get_db)
                          ):
    user = await crud.create_user(db, user)
    return user
# vytvořit if statement, kdyby username už existovalo
# bude se muset upravit model/schema, nebo oboje?


@app.get("/users/{user_id}", response_model=schemas.UserBase)
async def get_user_by_id(user_id: int,
                         db: AsyncSession = Depends(database.get_db)
                         ) -> schemas.UserBase:
    user_query = await crud.get_user(db, user_id)
    if user_query:
        return user_query
    raise HTTPException(status_code=404, detail="User ID does not exists!")

# get all trainings pro useless
# @app.get("/trainings/", response_model= list[schemas.TrainingRead])
# async def get_all_trainings(db: AsyncSession = Depends(database.get_db)):
#     return await crud.get_trainings(db)


@app.get("/trainings/{training_id}", response_model=schemas.TrainingRead)
async def get_training_by_id(training_id: int,
                             db: AsyncSession = Depends(database.get_db)
                             ):
    training = await crud.get_training(db, training_id)
    if not training:
        raise HTTPException(status_code=404, detail="Blbý ID tréningu")
    return training  # exercises already loaded


@app.post("/trainings/", response_model=schemas.TrainingCreateForUser)
async def create_new_training(training: schemas.TrainingCreateForUser,
                              db: AsyncSession = Depends(database.get_db)
                              ):
    new_user_training = await crud.create_training(db, training)
    return new_user_training

#OK
@app.post("/exercises/", response_model=schemas.ExerciseCreate)
async def create_new_exercise(exercise: schemas.ExerciseCreate,
                              db: AsyncSession = Depends(database.get_db)
                              ):
    new_exercise = await crud. create_exercise(db, exercise)
    return new_exercise

#OK
@app.get("/exercises/{exercise_id}", response_model = schemas.ExerciseRead)
async def get_exercise_by_id(exercise_id: int,
                             db: AsyncSession = Depends(database.get_db)):
    exercise = await crud.get_exercise(db, exercise_id)
    if exercise is None:
            raise HTTPException(status_code=404, detail='Blbý ID cviku')
    return exercise

#funguje, ale dodělat
@app.get("/exercises/", response_model= list[schemas.ExerciseRead])
async def get_all_exercises(db: AsyncSession = Depends(database.get_db)):
    exercises_query = await crud.get_exercises(db)
    return exercises_query
#když se nevyplní type, description je Null a není string, v tu chvíli nefungije get

"""
přidá sice exercise k training, ale všechny mají stejný počet opakování, váhu, poznámku
"""
@app.post("/trainings/{training_id}/exercises/", response_model=schemas.TrainingExerciseBase)
def add_exercises_to_training(training_id: int,
                              exercise_id: int,
                              exercise_to_add: schemas.TrainingExerciseCreate,
                              db: AsyncSession = Depends(database.get_db)
                              ):
    return crud.add_exercise_to_trainings(db, training_id, exercise_id, exercise_to_add)



 #vytvořit schemu pro to čtení exercise v tréninku



# printne routy
def list_routes(app):
    for route in app.routes:
        methods = ", ".join(route.methods)
        print(f"{methods:10s} {route.path}")

list_routes(app)
