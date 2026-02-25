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
   .venv\Scripts\Activate.ps1
   ```
3. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

## Çalıştırma

Aşağıdaki komut ile sunucuyu başlatabilirsiniz:

```bash
uvicorn app.main:app --reload
```

Sunucu başlatıldığında, aşağıdaki adreslerden API'ye erişebilirsiniz:
- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs


## Proje Yapısı

```
HabitTracker - Copy/
├── alembic.ini
├── README.md
├── requirements.txt
├── app/
│   ├── main.py
│   ├── config/
│   ├── controllers/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   └── services/
├── migrations/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
```

## Notlar
- Veritabanı olarak varsayılan olarak SQLite kullanılabilir, ancak yapılandırmaya göre farklı bir veritabanı da kullanılabilir.

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır.


