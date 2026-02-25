from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.schemas.progress import ProgressCreate, ProgressRead
from app.services.progress_service import create_progress_service, get_progress_service, mark_completed_service, delete_progress_service


router = APIRouter(tags=["Progress"])


@router.post("/habits/{habit_id}/progress/", response_model=ProgressRead, status_code=201)
def create_progress(habit_id: int, data: ProgressCreate, db: Session = Depends(get_db)):
    return create_progress_service(db, habit_id, data.date)


@router.get("/habits/{habit_id}/progress/", response_model=List[ProgressRead])
def get_progress(
    habit_id: int,
    db: Session = Depends(get_db),
    limit: int = 10,
    offset: int = 0
):
    return get_progress_service(db, habit_id, limit=limit, offset=offset)


@router.patch("/progress/{progress_id}/complete", response_model=ProgressRead)
def complete_progress(progress_id: int, db: Session = Depends(get_db)):
    return mark_completed_service(db, progress_id)


@router.delete("/progress/{progress_id}")
def delete_progress(progress_id: int, db: Session = Depends(get_db)):
    delete_progress_service(db, progress_id)
    return {"message": "İlerleme kaydı silindi."}
