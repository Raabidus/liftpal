
"""
tool pro vytváření testovácích záznamů v db
"""

from .database import engine, Base, DBSession
from .models import User, Exercise, Training, TrainingExercise

Base.metadata.create_all(engine)

session = DBSession()

# list_exercises_ids = [8, 9, 10, 11]

# new_user = User(username='TestUser', is_active=True)
# session.add(new_user)
# session.flush()

# new_training = Training(training_name='Full body A', training_type='FULL BODY', date='2025-08-01', note='testovací uživatel pro dotaty z api',
#                         user_id=new_user.id)
# session.add(new_training)
# session.flush()

# new_exercise_b = Exercise(name='Incline dumbells bench press', description='Incline 30-45 degree', muscle_group='ches', type='Push')
# new_exercise_a = Exercise(name='Barbell row', description='Clasic barbell row', muscle_group='back', type='Pull')
# session.add_all(new_exercise_b, new_exercise_a)

# new_training_exercises = [
#     TrainingExercise(training_id=new_training.id, exercise_id=eid, sets='5', reps='5', note='tohle musím doladit')
#     for eid in list_exercises_ids
#                                           ]
# session.add_all(new_training_exercises)
# session.flush()







