from fastapi import APIRouter
from models import Workout


router = APIRouter()


workouts = []

# get operations 


@router.get("/workouts")
def get_workouts():
    return workouts

@router.get("/workouts/category/{workout_category}")
def get_workouts_by_category(workout_category: str):
    for workout in workouts:
        if workout["category"] == workout_category:
            return workout
    return {"error": "Workout not found"}

@router.get("/workouts/{workout_id}")
def get_workout(workout_id: int):
    for workout in workouts:
        if workout["id"] == workout_id:
            return workout
    return {"error": "Workout not found"}

@router.get("/workouts/{workout_id}/total-burned")
def get_total_burned_calories(workout_id: int):
    for workout in workouts:
        if workout["id"] == workout_id:
            total_burned_calories = workout["duration_minutes"] * workout["burn_calories_per_minute"]

            if workout["category"] == "strength":
                total_burned_calories *= 1.1

            return {"total_burned_calories": total_burned_calories}
    return {"error": "Workout not found"}

# post operations

@router.post("/workouts")
def add_workouts(workout: Workout):

    workouts.append(workout.model_dump())

    return workouts


# delete operations

@router.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    for workout in workouts:
        if workout["id"] == workout_id:
            workouts.remove(workout)
            return "workout deleted"
    return {"error": "Workout not found"}



# put operations


@router.put("/workouts/{workout_id}")
def update_workout(workout_id: int, new_workout: Workout):
    for index, workout in enumerate(workouts):
        if workout["id"] == workout_id:
            workouts[index] = new_workout.model_dump()
            return workouts[index]

    return {"error": "Workout not found"}