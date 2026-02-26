from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.progress_repository import (
    count_progress_by_habit,
    create_progress,
    delete_progress,
    get_progress_by_habit,
    get_progress_by_id,
    mark_completed,
)
from app.repositories.habit_repository import get_habit_by_id


def create_progress_service(db: Session, habit_id: int, date):
    habit = get_habit_by_id(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Alışkanlık bulunamadı.")
    return create_progress(db, habit_id, date)


def get_progress_service(db: Session, habit_id: int, limit: int = 10, offset: int = 0):
    habit = get_habit_by_id(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Alışkanlık bulunamadı.")
    progress_items = get_progress_by_habit(db, habit_id, limit=limit, offset=offset)
    total = count_progress_by_habit(db, habit_id)
    return progress_items, total


def mark_completed_service(db: Session, progress_id: int):
    progress = get_progress_by_id(db, progress_id)
    if not progress:
        raise HTTPException(status_code=404, detail="İlerleme kaydı bulunamadı.")
    return mark_completed(db, progress_id)


def delete_progress_service(db: Session, progress_id: int):
    progress = get_progress_by_id(db, progress_id)
    if not progress:
        raise HTTPException(status_code=404, detail="İlerleme kaydı bulunamadı.")
    return delete_progress(db, progress_id)
