from typing import Iterable

from sqlalchemy.orm import Session

from repositories.user_repository import create_user, get_users
from schemas.user import UserCreate


def list_users(db: Session):
    return get_users(db)


def register_user(db: Session, user_in: UserCreate):
    # Buraya şifre hashleme, ekstra validasyon vs. eklenebilir
    return create_user(db, user_in)

