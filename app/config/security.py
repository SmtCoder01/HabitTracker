from passlib.context import CryptContext

# bcrypt 72 byte sınırı yerine, sınırı olmayan pbkdf2_sha256 kullanıyoruz
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


# şifre doğrulama
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

