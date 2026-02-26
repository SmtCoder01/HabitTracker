from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.pagination_config import PaginationConfig
from app.models.user import User
from app.schemas.base_response import BaseResponse
from app.schemas.pagination import PaginationDto
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.user_service import (
    create_user_service,
    delete_user_service,
    get_user_service,
    get_users_service,
    update_user_service,
)


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, data.name, data.surname, data.username, data.email, data.password)


@router.get("/", response_model=BaseResponse)
def get_users(
    db: Session = Depends(get_db),
    limit: int = PaginationConfig.DEFAULT_LIMIT,
    offset: int = PaginationConfig.DEFAULT_OFFSET,
    page: int = PaginationConfig.DEFAULT_PAGE,
):
    users = get_users_service(db, limit=limit, offset=offset)
    users_read = [UserRead.model_validate(u) for u in users]
    total = db.query(User).count()
    has_next_page = (offset + limit) < total
    has_previous_page = offset > 0

    pagination = PaginationDto(
        total=total,
        page=page,
        size=limit,
        HasNextPage=has_next_page,
        HasPreviousPage=has_previous_page,
    )

    response = BaseResponse(
        Success=True,
        Data={"users": users_read},
        Message=None,
        Errors=None,
        pagination=pagination,
    )
    return response


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_service(db, user_id)


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return update_user_service(db, user_id, data.name, data.surname, data.username, data.email, data.password)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_service(db, user_id)

