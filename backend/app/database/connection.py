"""
Database connection module for Revolution X
TimescaleDB optimized for Ubuntu 24.04
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from app.config import settings

# Convert PostgreSQL URL to async version
def get_async_database_url(url: str) -> str:
    """Convert sync PostgreSQL URL to async."""
    return url.replace("postgresql://", "postgresql+asyncpg://")

# Create async engine
async_engine = create_async_engine(
    get_async_database_url(settings.DATABASE_URL),
    echo=settings.DEBUG,
    pool_size=settings.DB_POOL_SIZE,
    max_overflow=settings.DB_MAX_OVERFLOW,
    pool_pre_ping=True,  # Verify connections before using
    pool_recycle=3600,   # Recycle connections after 1 hour
)

# Create async session factory
AsyncSessionLocal = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Base class for models
Base = declarative_base()


async def init_db():
    """
    Initialize database tables.
    Called on application startup.
    """
    async with async_engine.begin() as conn:
        # Create all tables
        # await conn.run_sync(Base.metadata.create_all)
        pass  # Will use Alembic migrations in production


async def close_db():
    """
    Close database connections.
    Called on application shutdown.
    """
    await async_engine.dispose()


async def get_db_session() -> AsyncSession:
    """
    Get a database session.
    Use as context manager.
    """
    async with AsyncSessionLocal() as session:
        return session
