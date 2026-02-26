from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.habit_repository import create_habit, get_habits_by_user, get_habit_by_id, delete_habit
from app.config.pagination_config import PaginationConfig
from app.repositories.user_repository import get_user_by_id


def create_habit_service(db: Session, user_id: int, title: str, description: str = None):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    return create_habit(db, user_id, title, description)


def get_habits_service(db: Session, user_id: int, limit: int = PaginationConfig.DEFAULT_LIMIT, offset: int = PaginationConfig.DEFAULT_OFFSET):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    return get_habits_by_user(db, user_id, limit=limit, offset=offset)


def get_habit_service(db: Session, habit_id: int):
    habit = get_habit_by_id(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Alışkanlık bulunamadı.")
    return habit


def delete_habit_service(db: Session, habit_id: int):
    habit = get_habit_by_id(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Alışkanlık bulunamadı.")
    return delete_habit(db, habit_id)
