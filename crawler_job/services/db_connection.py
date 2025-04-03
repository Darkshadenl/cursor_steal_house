import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection settings
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")

# Create database URL (note the postgresql+asyncpg:// prefix)
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Create async engine
engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Enable the connection pool "pre-ping" feature
    pool_recycle=3600,  # Recycle connections after 1 hour
    echo=False,  # Set to True for SQL query logging
)

# Create async session factory
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Base class for models
Base = declarative_base()


def get_db_session() -> AsyncSession:
    """
    Get a new database session (non-async function for use in synchronous contexts).

    Returns:
        AsyncSession: A new async session that should be closed by the caller.
    """
    return AsyncSessionLocal()


async def get_db_context():
    """
    Async context manager for database sessions.

    Usage:
        async with get_db_context() as session:
            # Use session for database operations
    """
    session = AsyncSessionLocal()
    try:
        yield session
    finally:
        await session.close()
