from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.services.user_service import create_user_service, get_users_service, get_user_service, update_user_service, delete_user_service
from app.schemas.user import UserCreate, UserUpdate, UserRead
from typing import List


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, data.name, data.surname, data.username, data.email, data.password)


@router.get("/", response_model=List[UserRead])
def get_users(
    db: Session = Depends(get_db),
    limit: int = 10,
    offset: int = 0
):
    return get_users_service(db, limit=limit, offset=offset)


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_service(db, user_id)


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return update_user_service(db, user_id, data.name, data.surname, data.username, data.email, data.password)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_service(db, user_id)

