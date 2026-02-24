from sqlalchemy import Column, Integer, String, ForeignKey,Boolean,DateTime,UniqueConstraint
from sqlalchemy.orm import relationship
from app.config.database import Base
from app.models.base import BaseModel


class Progress(BaseModel):
    __tablename__ = "progress"

    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    completed = Column(Boolean, default=False)

    habit = relationship("Habit", back_populates="progress")


    # Her habit için aynı gün sadece bir progress kaydı olmasını sağlamak için unique constraint ekliyoruz
    __table_args__ = (
        UniqueConstraint("habit_id", "date", name="uix_habit_date"),)