from fastapi import FastAPI
from routes.workouts import router as w_router


app = FastAPI()

app.include_router(w_router)