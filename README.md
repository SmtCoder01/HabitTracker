# HabitTracker (Hilal-Cansu)

Bu proje, alışkanlık takibi yapmak için geliştirilmiş bir FastAPI tabanlı backend uygulamasıdır.

## Özellikler
- Kullanıcı yönetimi (kayıt, giriş, profil)
- Alışkanlık ekleme, listeleme, güncelleme, silme
- Alışkanlık ilerleme takibi
- Sağlık kontrolü (health check)

## Kurulum

1. **Depoyu klonlayın:**
   ```bash
   git clone <repo-url>
   cd HabitTrackerBackend-main/HabitTrackerBackend-main
   ```
2. **Sanal ortamı oluşturun ve etkinleştirin:**
   ```bash
   python -m venv .venv
   # Windows için:
   .venv\Scripts\activate
   ```
3. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

## Çalıştırma

Aşağıdaki komut ile sunucuyu başlatabilirsiniz:

```bash
uvicorn main:app --reload
```

Sunucu başlatıldığında, aşağıdaki adreslerden API'ye erişebilirsiniz:
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

## Proje Yapısı

```
HabitTrackerBackend-main/
├── main.py
├── requirements.txt
├── config/
├── controllers/
├── models/
├── repositories/
├── schemas/
├── services/
└── habits.db
```

## Notlar
- Pydantic v2 ile ilgili uyarı: `orm_mode` yerine `from_attributes` kullanılması önerilir.
- Veritabanı olarak SQLite kullanılmaktadır (habits.db).

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır.


