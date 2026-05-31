from fastapi import FastAPI

from database import Base, engine
from routes.workouts import router as w_router

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(w_router)
