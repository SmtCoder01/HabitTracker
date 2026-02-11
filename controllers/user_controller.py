from collections.abc import Generator

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import SessionLocal
from schemas.user import UserCreate, UserRead
from services.user_service import list_users, register_user


router = APIRouter()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[UserRead])
def read_users(db: Session = Depends(get_db)):
    return list_users(db)


@router.post("/", response_model=UserRead)
def create_user_endpoint(user_in: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_in)

