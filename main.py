from fastapi import FastAPI
from routes.workouts import router as w_router
from database import engine, Base
import db_models

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(w_router)