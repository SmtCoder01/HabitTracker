from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ProgressCreate(BaseModel):
    date: datetime


class ProgressRead(BaseModel):
    id: int
    habit_id: int
    date: datetime
    completed: bool

    model_config = ConfigDict(from_attributes=True)
