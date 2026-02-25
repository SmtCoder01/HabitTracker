from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Sadece Pydantic'in BaseModel'i kullanılacak
class ProgressCreate(BaseModel):
    date: datetime

class ProgressRead(BaseModel):
    id: int
    habit_id: int
    date: datetime
    completed: bool

    model_config = ConfigDict(from_attributes=True)
