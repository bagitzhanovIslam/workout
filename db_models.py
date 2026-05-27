from sqlalchemy import Column, Integer, String
from database import Base

class WorkoutDB(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)
    category = Column(String)
    duration_minutes = Column(Integer)
    burn_calories_per_minute = Column(Integer)
    repeats = Column(Integer)
