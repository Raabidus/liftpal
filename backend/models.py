"""
models.py
- SQLALCHEMY models
"""

from sqlalchemy import Integer, String, Float, Column, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .database import Base

#TODO
#přídat password - zjistit jak to zashovat
#rozšířit model training o typ (push, pull, fb, ...) a custom name (pojmenování)




class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    is_active = Column(Boolean, nullable=False, default=False)
    # password = 

    trainings = relationship('Training', back_populates='user')


class Exercise(Base):
    __tablename__ = 'exercises'
    exercise_id = Column(Integer, primary_key=True)
    exercise_name = Column(String, nullable=False)
    description = Column(String)
    muscle_group = Column(String) #muslce_group by se dalo předělat, aby nebylo str ale list partii - pro budoucí filtry
    exercise_type = Column(String)

    training_exercises = relationship('TrainingExercise', back_populates='exercise')


class Training(Base):
    __tablename__ = 'trainings'
    training_id = Column(Integer, primary_key=True)
    training_name = Column(String, nullable=False)
    training_type = Column(String(32), nullable=True)
    date = Column(Date)
    note = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    user = relationship('User', back_populates='trainings')
    exercises = relationship('TrainingExercise', back_populates='training')


class TrainingExercise(Base):
    __tablename__ = 'training_exercises'
    training_exercises_id = Column(Integer, primary_key=True)
    sets = Column(Integer)
    reps = Column(String)
    weight = Column(Float)
    order = Column(Integer, nullable=True)
    note = Column(String(255), nullable=True)
    training_id = Column(Integer, ForeignKey('trainings.training_id'))
    exercise_id = Column(Integer, ForeignKey('exercises.exercise_id'))

    training = relationship('Training', back_populates='exercises')
    exercise = relationship('Exercise', back_populates='training_exercises')





    







