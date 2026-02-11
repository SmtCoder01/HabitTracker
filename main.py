from fastapi import FastAPI

from config.database import Base, engine
from controllers.user_controller import router as user_router
from models import User  # noqa: F401


app = FastAPI(
    title="Habit Tracker API",
    version="0.1.0",
)


@app.on_event("startup")
def on_startup() -> None:
    # Tüm modeller için tabloları oluştur
    Base.metadata.create_all(bind=engine)


@app.get("/health", tags=["health"])
def health_check() -> dict:
    return {"status": "ok"}


app.include_router(user_router, prefix="/users", tags=["users"])

