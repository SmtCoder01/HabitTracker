from sqlalchemy.orm import Session
from app.models.user import User


def create_user(db: Session, name: str, surname: str, username: str, email: str, password: str):
    user = User(name=name, surname=surname, username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_all_users(db: Session, limit: int = 10, offset: int = 0):
    return db.query(User).offset(offset).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def update_user(db:Session, user_id: int, name: str = None, surname: str = None, username: str = None, email: str = None, password: str = None):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    if name is not None:
        user.name = name
    if surname is not None:
        user.surname = surname
    if username is not None:
        user.username = username
    if email is not None:
        user.email = email
    if password is not None:
        user.password = password
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    
    db.delete(user)
    db.commit()
        
    return user
