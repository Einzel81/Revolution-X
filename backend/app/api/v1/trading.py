"""
Trading API endpoints
Phase 1: Basic structure
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db

router = APIRouter()


@router.get("/status")
async def trading_status():
    """Get trading system status."""
    return {
        "status": "operational",
        "mode": "manual",  # Will be dynamic in Phase 3
        "active": False,
        "message": "Trading system ready for Phase 3",
    }


@router.get("/account")
async def account_info():
    """Get trading account info."""
    # TODO: Implement in Phase 3
    return {
        "balance": 0.0,
        "equity": 0.0,
        "margin": 0.0,
        "free_margin": 0.0,
        "message": "Connect MT5 for live data",
    }
