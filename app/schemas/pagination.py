from typing import Optional

class PaginationDto:
    """
    Sayfalama bilgilerini tutan veri transfer objesi.
    total: Toplam kayıt sayısı
    page: Mevcut sayfa numarası
    size: Sayfa başına gösterilecek kayıt sayısı
    has_next_page: Sonraki sayfa var mı?
    has_previous_page: Önceki sayfa var mı?
    """
    def __init__(self, total: int, page: int, size: int, has_next_page: bool, has_previous_page: bool):
        self.total = total
        self.page = page
        self.size = size
        self.has_next_page = has_next_page
        self.has_previous_page = has_previous_page

    def dict(self):
        return {
            "total": self.total,
            "page": self.page,
            "size": self.size,
            "has_next_page": self.has_next_page,
            "has_previous_page": self.has_previous_page
        }
