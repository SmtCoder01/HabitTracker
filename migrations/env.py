from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Bu, Alembic Config nesnesidir, kullanılan .ini dosyasındaki değerlere erişim sağlar.
config = context.config

# Python loglaması için config dosyasını yorumlar.
# Bu satır temelde loglayıcıları kurar.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Modelinizin MetaData nesnesini buraya ekleyin
# 'autogenerate' desteği için
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from config.database import Base
from models import user
target_metadata = Base.metadata

# env.py'nin ihtiyaçlarına göre tanımlanan diğer değerler buradan alınabilir:
# my_important_option = config.get_main_option("my_important_option")
# ... vb.


def run_migrations_offline() -> None:
    """Migrationları 'offline' modda çalıştırır.

    Bu, context'i sadece bir URL ile yapılandırır,
    Engine oluşturulmaz, fakat Engine de kabul edilebilir.
    Engine oluşturmayı atladığımız için DBAPI'ye gerek yoktur.

    Buradaki context.execute() çağrıları verilen stringi
    script çıktısına yazar.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Migrationları 'online' modda çalıştırır.

    Bu senaryoda bir Engine oluşturulup
    context ile ilişkilendirilir.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
