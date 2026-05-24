from pydantic import BaseModel

class Workout(BaseModel):
    id: int
    exercise_name: str
    category: str
    duration_minutes: int
    burn_calories_per_minute: int
    repeats: int