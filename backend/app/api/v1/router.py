"""
API v1 router aggregator
"""

from fastapi import APIRouter

from app.api.v1 import trading, signals

api_router = APIRouter()

# Include sub-routers
api_router.include_router(trading.router, prefix="/trading", tags=["trading"])
api_router.include_router(signals.router, prefix="/signals", tags=["signals"])
