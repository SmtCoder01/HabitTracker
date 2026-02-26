from pydantic import BaseModel


class PaginationDto(BaseModel):
    """
    Sayfalama bilgilerini tutan veri transfer objesi.
    total: Toplam kayıt sayısı (COUNT ile alınır)
    page: Mevcut sayfa numarası
    size: Sayfa başına gösterilecek kayıt sayısı
    HasNextPage: Sonraki sayfa var mı?
    HasPreviousPage: Önceki sayfa var mı?
    """

    total: int
    page: int
    size: int
    HasNextPage: bool
    HasPreviousPage: bool
