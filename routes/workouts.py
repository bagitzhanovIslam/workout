from fastapi import APIRouter, HTTPException
from models import Workout, WorkoutResponse
from database import SessionLocal
from db_models import WorkoutDB


router = APIRouter()

# get operations 

@router.get("/workouts", response_model=list[WorkoutResponse])
def get_workouts():
    
    db = SessionLocal()

    workouts = db.query(WorkoutDB).all()

    db.close()

    return workouts


@router.get("/workouts/category/{workout_category}", response_model=list[WorkoutResponse])
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
        raise HTTPException(status_code=404, detail="Workout not found")
    
    total_burned_calories = workout.duration_minutes * workout.burn_calories_per_minute

    if workout.category == "strength":
        total_burned_calories *= 1.1
    
    db.close()

    return {"total_burned_calories": total_burned_calories}


@router.get("/workouts/{workout_id}", response_model=WorkoutResponse)
def get_workout_by_id(workout_id: int):
    
    db = SessionLocal()
    
    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()

    
    if workout is None:
        db.close()
        raise HTTPException(status_code=404, detail="Workout not found")

    db.close()
    return workout



 # post operations


@router.post("/workouts", response_model=WorkoutResponse, status_code=201)
def add_workout(workout: Workout):

    db = SessionLocal()

    new_workout = WorkoutDB(
        id = workout.id,
        exercise_name = workout.exercise_name,
        category = workout.category,
        duration_minutes = workout.duration_minutes,
        burn_calories_per_minute = workout.burn_calories_per_minute,
        repeats = workout.repeats
    )

    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)

    return new_workout



 # delete operations


@router.delete("/workouts/{workout_id}", status_code=204)
def delete_workout(workout_id: int):
    
    db = SessionLocal()

    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()

    if workout is None:
        db.close()
        raise HTTPException(status_code=404, detail="Workout not found")
    
    db.delete(workout)
    db.commit()
    db.close()

    return



# put operations


@router.put("/workouts/{workout_id}", response_model=WorkoutResponse)
def update_workout(workout_id: int, new_workout: Workout):

    db = SessionLocal()

    workout = db.query(WorkoutDB).filter(WorkoutDB.id == workout_id).first()

    if workout is None:
        db.close()
        raise HTTPException(status_code=404, detail="Workout not found")
    
    workout.exercise_name = new_workout.exercise_name
    workout.category = new_workout.category
    workout.duration_minutes = new_workout.duration_minutes
    workout.burn_calories_per_minute = new_workout.burn_calories_per_minute
    workout.repeats = new_workout.repeats

    db.commit()
    db.refresh(workout)
    db.close()

    return workout