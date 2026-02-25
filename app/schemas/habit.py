from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# Sadece Pydantic'in BaseModel'i kullanılacak
class HabitCreate(BaseModel):
    title: str
    description: Optional[str] = None

class HabitRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    user_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
