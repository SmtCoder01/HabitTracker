import logging
logging.basicConfig(level=logging.DEBUG)
from fastapi import FastAPI
from app.config.database import engine, Base
#modelleri import ediyoruz ki tablolar oluşsun
from app.models import User, Habit, Progress

from app.controllers.user_controller import router as user_router
from app.controllers.habit_controller import router as habit_router
from app.controllers.progress_controller import router as progress_router

app = FastAPI(title="Habit Tracker API")

Base.metadata.create_all(bind=engine)
#endpointleri ekliyoruz
app.include_router(user_router)
app.include_router(habit_router)
app.include_router(progress_router)

@app.get("/")
def root():
    return {"message": "Habit Tracker Running"}