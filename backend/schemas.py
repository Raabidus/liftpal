from pydantic import BaseModel, Field
from typing import Optional, Annotated, List

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

# --- Training schemas ---
class TrainingBase(BaseModel):
    training_id: int
    training_name: str

class TrainingCreateForUser(BaseModel):
    training_name: str
    user_id: int

    class config:
        from_attribute = True

class TrainingRead(TrainingBase):

    class ConfigDict:
        arbitrary_types_allowed = True

class UserTrainingRead(BaseModel):
    user_id: int
    username:str
    trainings: List[TrainingRead] = [] #list vše tréninkl daného uživatele

    class ConfigDict:
        arbitrary_types_allowed = True

# --- Exercise Schemas ---
class ExerciseBase(BaseModel):
    exercise_id: int
    exercise_type: str
    exercise_name: str

class ExerciseAddToTraining(BaseModel):
    training_id: int
    exercise_type: str
    exercise_name: str






# class User(BaseModel):
#     user: str = Field(min_length=3, max_length=20)
#     is_active: Optional[bool] = False
#     training_ids: Optional[list[int]] = Field(default_factory=list)

# # doplnit
# class Training(BaseModel):
#     training: str = Field(min_length=2, max_length=20)
#     pass

# # TE spíš rozdělit?
# # udělat schema na TE jako základ a pak info k tréninku?
# class TrainingExercise(BaseModel):
#     pass

