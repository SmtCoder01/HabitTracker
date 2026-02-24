from sqlalchemy.orm import Session
from app.models.progress import Progress


def create_progress(db: Session, habit_id: int, date):
    progress = Progress(habit_id=habit_id, date=date)
    db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress


def get_progress_by_habit(db: Session, habit_id: int):
    return db.query(Progress).filter(Progress.habit_id == habit_id).all()


def get_progress_by_id(db: Session, progress_id: int):
    return db.query(Progress).filter(Progress.id == progress_id).first()


def mark_completed(db: Session, progress_id: int):
    progress = get_progress_by_id(db, progress_id)
    if progress:
        progress.completed = True
        db.commit()
        db.refresh(progress)
    return progress


def delete_progress(db: Session, progress_id: int):
    progress = get_progress_by_id(db, progress_id)
    if progress:
        db.delete(progress)
        db.commit()
    return progress


