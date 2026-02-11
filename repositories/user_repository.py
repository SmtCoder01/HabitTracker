from typing import Iterable

from sqlalchemy.orm import Session

from models.user import User
from schemas.user import UserCreate


def get_users(db: Session) -> Iterable[User]:
    return db.query(User).all()


def create_user(db: Session, user_in: UserCreate) -> User:
    user = User(email=user_in.email, full_name=user_in.full_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

