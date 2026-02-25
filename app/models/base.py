from sqlalchemy import Column, Integer, String,DateTime
from app.config.database import Base    
from datetime import datetime, timezone


from sqlalchemy import Column, Integer, DateTime
from app.config.database import Base
from datetime import datetime, timezone


class BaseModel(Base):
    __abstract__ = True  # Bu sınıfın doğrudan tablo oluşturmayacağını belirtir

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))