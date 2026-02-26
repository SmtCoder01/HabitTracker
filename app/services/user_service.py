from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.config.security import hash_password
from app.repositories.user_repository import (
    count_users,
    create_user,
    delete_user,
    get_all_users,
    get_user_by_email,
    get_user_by_id,
    update_user,
)


def create_user_service(db: Session, name: str, surname: str, username: str, email: str, password: str):
    existing_user = get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Bu email zaten kayıtlı.")
    hashed_password = hash_password(password)
    return create_user(db, name, surname, username, email, hashed_password)


def get_users_service(db: Session, limit: int = 10, offset: int = 0):
    users = get_all_users(db, limit=limit, offset=offset)
    total = count_users(db)
    return users, total


def get_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    return user


def update_user_service(db: Session, user_id: int, name: str = None, surname: str = None, username: str = None, email: str = None, password: str = None):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    if password is not None:
        password = hash_password(password)
    return update_user(db, user_id, name, surname, username, email, password)


def delete_user_service(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı.")
    return delete_user(db, user_id)