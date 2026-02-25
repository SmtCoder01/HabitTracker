from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.schemas.habit import HabitCreate, HabitRead
from app.services.habit_service import create_habit_service, get_habits_service, get_habit_service, delete_habit_service


router = APIRouter(tags=["Habits"])


@router.post("/create_habit", response_model=HabitRead, status_code=201)
def create_habit(user_id: int, data: HabitCreate, db: Session = Depends(get_db)):
    return create_habit_service(db, user_id, data.title, data.description)


@router.get("/users/{user_id}/habits/", response_model=List[HabitRead])
def get_habits(
    user_id: int,
    db: Session = Depends(get_db),
    limit: int = 10,
    offset: int = 0
):
    return get_habits_service(db, user_id, limit=limit, offset=offset)


@router.get("/habits/{habit_id}", response_model=HabitRead)
def get_habit(habit_id: int, db: Session = Depends(get_db)):
    return get_habit_service(db, habit_id)


@router.delete("/delete_habit")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    delete_habit_service(db, habit_id)
    return {"message": "Alışkanlık silindi."}
