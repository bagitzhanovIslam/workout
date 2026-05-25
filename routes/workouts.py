from fastapi import APIRouter
from models import Workout
from database import SessionLocal
from db_models import WorkoutDB


router = APIRouter()


workouts = []

# get operations 

@router.get("/workouts")
def get_workouts():
    
    db = SessionLocal()

    workouts = db.query(WorkoutDB).all()

    db.close()

    return workouts


@router.get("/workouts/{workout_id}")
def get_workout_by_id(workout_id: int):
    
    db = SessionLocal()
    
    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()

    db.close()

    return workout

@router.get("/workouts/category/{workout_category}")
def get_workouts_by_category(workout_category: str):

    db = SessionLocal()

    workouts = db.query(WorkoutDB).filter(WorkoutDB.category == workout_category).all()

    db.close()

    return workouts


@router.get("/workouts/{workout_id}/total-burned")
def get_total_burned_calories(workout_id: int):

    db = SessionLocal()

    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()

    if workout is None:
        db.close()
        return {"error": "Workout not found"}
    
    total_burned_calories = workout.duration_minutes * workout.burn_calories_per_minute

    if workout.category == "strength":
        total_burned_calories *= 1.1
    
    db.close()

    return {"total_burned_calories": total_burned_calories}

 # post operations

@router.post("/workouts/db")
def add_workout(workout: Workout):

    db = SessionLocal()

    new_workout = WorkoutDB(
        id = workout.id,
        exercise_name = workout.exercise_name,
        category = workout.category,
        duration_minutes = workout.duration_minutes,
        burn_calories_per_minute = workout.burn_calories_per_minute
    )

    db.add(new_workout)
    db.commit()
    db.close()

    return {"message": "Workout added to database"}



 # delete operations


@router.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int):
    
    db = SessionLocal()

    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()

    if workout is None:
        db.close()
        return {"error": "Workout not found"}
    
    db.delete(workout)
    db.commit()
    db.close()

    return {"message": "Workout deleted"}


# put operations


@router.put("/workouts/{workout_id}")
def update_workout(workout_id: int, new_workout: Workout):

    db = SessionLocal()

    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()

    if workout is None:
        db.close()
        return {"error": "Workout not found"}
    
    workout.exercise_name = new_workout.exercise_name
    workout.category = new_workout.category
    workout.duration_minutes = new_workout.duration_minutes
    workout.burn_calories_per_minute = new_workout.burn_calories_per_minute

    db.commit()
    db.refresh(workout)
    db.close()

    return {"message": "Workout updated"}