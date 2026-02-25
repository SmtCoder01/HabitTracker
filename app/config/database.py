# Gerekli kütüphaneleri ekliyoruz
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
# .env dosyasını yükleyerek ortam değişkenlerini alıyoruz
load_dotenv()

# Veritabanı bağlantı adresini alıyoruz
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy engine oluşturuluyor
engine = create_engine(
    DATABASE_URL,
    echo=True  # SQL loglarını görürsün (dev için iyi)
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Tüm modellerin base'i
Base = declarative_base()

# FastAPI'de dependency olarak kullanılacak DB oturumu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()