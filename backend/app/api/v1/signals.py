"""
Signals API endpoints
Phase 1: Basic structure
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/latest")
async def latest_signals():
    """Get latest trading signals."""
    return {
        "signals": [],
        "message": "AI signals available in Phase 4",
    }


@router.get("/scanner")
async def scanner_status():
    """Get smart scanner status."""
    return {
        "status": "idle",
        "assets_scanned": [],
        "best_opportunity": None,
        "message": "Smart Scanner in Phase 4",
    }
