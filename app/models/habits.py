from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.models.base import BaseModel


class Habit(BaseModel):
    __tablename__ = "habits"

    title = Column(String, nullable=False)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="habits")

    progress = relationship("Progress", back_populates="habit", cascade="all,delete-orphan")