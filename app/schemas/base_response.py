from typing import Generic, TypeVar, Optional, List

T = TypeVar("T")

class BaseResponse(Generic[T]):
    def __init__(self, success: bool, data: Optional[T] = None, message: Optional[str] = None, errors: Optional[List[str]] = None, pagination: Optional[dict] = None):
        self.success = success
        self.data = data
        self.message = message
        self.errors = errors
        self.pagination = pagination

    def dict(self):
        return {
            "success": self.success,
            "data": self.data,
            "message": self.message,
            "errors": self.errors,
            "pagination": self.pagination
        }
