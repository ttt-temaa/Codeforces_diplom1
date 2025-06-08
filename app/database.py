# Модуль настройки и инициализации базы данных.

# Этот модуль отвечает за:
# 1. Создание асинхронного движка SQLAlchemy
# 2. Настройку фабрики сессий для работы с базой данных


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from constants import DB_USER, PASSWORD, HOST, PORT, DATABASE

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
