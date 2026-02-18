"""
Global dependencies for Revolution X
"""

from typing import AsyncGenerator

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import AsyncSessionLocal
from app.config import settings

# Security scheme
security = HTTPBearer(auto_error=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency for database sessions.
    Yields async session and ensures proper cleanup.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def get_current_user_optional(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    """
    Get current user from JWT token (optional).
    Returns empty dict if no valid token.
    """
    if not credentials:
        return {}
    
    # TODO: Implement JWT validation in Phase 2
    return {"id": "anonymous", "role": "guest"}


async def get_current_user_required(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    """
    Get current user from JWT token (required).
    Raises 401 if no valid token.
    """
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # TODO: Implement JWT validation in Phase 2
    return {"id": "user_id", "role": "trader"}
