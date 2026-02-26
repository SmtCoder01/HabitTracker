from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.config.pagination_config import PaginationConfig
from app.models.progress import Progress
from app.schemas.base_response import BaseResponse
from app.schemas.pagination import PaginationDto
from app.schemas.progress import ProgressCreate, ProgressRead
from app.services.progress_service import (
    create_progress_service,
    delete_progress_service,
    get_progress_service,
    mark_completed_service,
)


router = APIRouter(tags=["Progress"])


@router.post("/habits/{habit_id}/progress/", response_model=ProgressRead, status_code=201)
def create_progress(habit_id: int, data: ProgressCreate, db: Session = Depends(get_db)):
    return create_progress_service(db, habit_id, data.date)


@router.get("/habits/{habit_id}/progress/", response_model=BaseResponse)
def get_progress(
    habit_id: int,
    db: Session = Depends(get_db),
    limit: int = PaginationConfig.DEFAULT_LIMIT,
    offset: int = PaginationConfig.DEFAULT_OFFSET,
    page: int = PaginationConfig.DEFAULT_PAGE,
):
    progress_items = get_progress_service(db, habit_id, limit=limit, offset=offset)
    progress_read = [ProgressRead.model_validate(p) for p in progress_items]
    total = db.query(Progress).filter(Progress.habit_id == habit_id).count()
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
        Data={"progress": progress_read},
        Message=None,
        Errors=None,
        pagination=pagination,
    )
    return response


@router.patch("/progress/{progress_id}/complete", response_model=ProgressRead)
def complete_progress(progress_id: int, db: Session = Depends(get_db)):
    return mark_completed_service(db, progress_id)


@router.delete("/progress/{progress_id}")
def delete_progress(progress_id: int, db: Session = Depends(get_db)):
    delete_progress_service(db, progress_id)
    return {"message": "İlerleme kaydı silindi."}
