from typing import Literal

from pydantic import BaseModel, Field


class Workout(BaseModel):
    id: int
    exercise_name: str
    category: Literal["cardio", "strength", "stretching"]
    duration_minutes: int = Field(gt=0)
    burn_calories_per_minute: int = Field(gt=0)
    repeats: int = Field(gte=0)


class WorkoutResponse(BaseModel):
    id: int
    exercise_name: str
    category: str
    duration_minutes: int
    burn_calories_per_minute: int
    repeats: int

    class Config:
        from_attributes = True
