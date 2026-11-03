from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from collections.abc import AsyncGenerator
from src.core.settings import Settings

class Database:
    def __init__(self):
        self.settings = Settings()
        self.engine = create_async_engine(self.settings.DATABASE_URL, echo=True)
        self.SessionLocal = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.SessionLocal() as session:
            yield session