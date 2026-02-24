from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.user_repository import create_user, get_all_users, get_user_by_id, get_user_by_email, update_user, delete_user
from app.config.security import hash_password


def create_user_service(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Bu email zaten kayıtlı.")
    hashed_password = hash_password(password)
    return create_user(db, email, hashed_password)


def get_users_service(db: Session):
    return get_all_users(db)


def get_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    return user


def update_user_service(db: Session, user_id: int, email: str = None, password: str = None):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    if password is not None:
        password = hash_password(password)
    return update_user(db, user_id, email, password)


def delete_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    return delete_user(db, user_id)