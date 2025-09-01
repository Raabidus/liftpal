from pydantic import BaseModel, Field

from typing import Optional, Annotated, List

from datetime import date

#TODO


# Field slouží k nastavení min, max, výchozích hodnot atp. - doplnit jak bude potřeba
# constr slouží ke kontole strinhů, všehno malym, bez mezer...
# zjistit jak/kde použíz orm_mode = True - používat u dotazů do db, např. UserInfo - vrátí info z db v ORM modelu Pydantic čeká dict
# bude potřeba ještě:
#    UserTrainings, UserTrainingExercises, ...
"""
možná bude u class potřeba použít namísto
    class ConfigDict:
        arbitrary_types_allowed = True

    class config:
        from_attribute = True

důvod je, že asi nepoužívám arbitary typy - ověřit
"""

# --- User Schemas ---
class UserBase(BaseModel):
   user_id: int
   username: str

class UserCreate(UserBase):
    pass

# class GetUser(UserBase):
#     user_id: int

# --- Training schemas ---
class TrainingBase(BaseModel):
    training_id: int
    training_name: str
    training_type: str
    date: date
    note: str

class TrainingCreateForUser(BaseModel):
    training_name: str
    training_type: Optional[str] = None # není povinné může být None
    date: date
    note: Optional[str] = None
    user_id: int

    class config:
        from_attribute = True

class TrainingRead(TrainingBase):

    class config:
        from_attribute = True
    # class ConfigDict:
    #     arbitrary_types_allowed = True

class UserTrainingRead(BaseModel):
    user_id: int
    username:str
    trainings: List[TrainingRead] = [] #list všech tréninků daného uživatele

    class ConfigDict:
        arbitrary_types_allowed = True

#dodělat/vymyslet
class TrainingExercise(BaseModel):
    pass

# --- Exercise Schemas ---
class ExerciseBase(BaseModel):
    exercise_id: int
    exercise_type: str
    exercise_name: str
    description: str
    muscle_group: str #muslce_group by se dalo předělat, aby nebylo str ale list partii - pro budoucí filtry
    #když se nevyplní type, description je Null a není string, v tu chvíli nefungije get

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseRead(ExerciseBase):

    class config:
        from_attribute = True

class ExerciseAddToTraining(BaseModel):
    training_id: int
    exercise_type: str
    exercise_name: str








# # TE spíš rozdělit?
# # udělat schema na TE jako základ a pak info k tréninku?
# class TrainingExercise(BaseModel):
#     pass

