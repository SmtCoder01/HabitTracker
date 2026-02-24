from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.models.base import BaseModel



class User(BaseModel):
    __tablename__ = "users"

    
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    # İlişkiler
    habits = relationship("Habit", back_populates="user", cascade="all,delete-orphan")


