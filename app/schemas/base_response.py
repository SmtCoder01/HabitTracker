from typing import Any, List, Optional

from pydantic import BaseModel

from app.schemas.pagination import PaginationDto


class BaseResponse(BaseModel):
    """
    Tüm list ve genel cevaplar için kullanılacak temel response modeli.

    Success: İşlem başarılı mı?
    Message: Kullanıcıya gösterilecek mesaj (opsiyonel)
    Data: Asıl veri (liste veya tek obje)
    Errors: Hata mesajları listesi (opsiyonel)
    pagination: Sayfalama bilgileri (opsiyonel)
    """

    Success: bool
    Message: Optional[str] = None
    Data: Optional[Any] = None
    Errors: Optional[List[str]] = None
    pagination: Optional[PaginationDto] = None
