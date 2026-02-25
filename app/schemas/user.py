from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime

# Sadece Pydantic'in BaseModel'i kullanılacak
class UserCreate(BaseModel):
    name: str
    surname: str
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: str | None = None
    surname: str | None = None
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UserRead(BaseModel):
    id: int
    name: str
    surname: str
    username: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

