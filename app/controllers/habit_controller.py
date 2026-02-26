from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.pagination_config import PaginationConfig
from app.models.habits import Habit
from app.schemas.base_response import BaseResponse
from app.schemas.habit import HabitCreate, HabitRead
from app.schemas.pagination import PaginationDto
from app.services.habit_service import (
    create_habit_service,
    delete_habit_service,
    get_habit_service,
    get_habits_service,
)


router = APIRouter(tags=["Habits"])


@router.post("/create_habit", response_model=HabitRead, status_code=201)
def create_habit(user_id: int, data: HabitCreate, db: Session = Depends(get_db)):
    return create_habit_service(db, user_id, data.title, data.description)


@router.get("/users/{user_id}/habits/", response_model=BaseResponse)
def get_habits(
    user_id: int,
    db: Session = Depends(get_db),
    limit: int = PaginationConfig.DEFAULT_LIMIT,
    offset: int = PaginationConfig.DEFAULT_OFFSET,
    page: int = PaginationConfig.DEFAULT_PAGE
):
    habits = get_habits_service(db, user_id, limit=limit, offset=offset)
    total = db.query(Habit).filter(Habit.user_id == user_id).count()
    has_next_page = (offset + limit) < total
    has_previous_page = offset > 0
    pagination = PaginationDto(
        total=total,
        page=page,
        size=limit,
        HasNextPage=has_next_page,
        HasPreviousPage=has_previous_page
    )
    response = BaseResponse(
        Success=True,
        Data={"habits": habits},
        Message=None,
        Errors=None,
        pagination=pagination
    )
    return response


@router.get("/habits/{habit_id}", response_model=HabitRead)
def get_habit(habit_id: int, db: Session = Depends(get_db)):
    return get_habit_service(db, habit_id)


@router.delete("/delete_habit")
def delete_habit(habit_id: int, db: Session = Depends(get_db)):
    delete_habit_service(db, habit_id)
    return {"message": "Alışkanlık silindi."}
