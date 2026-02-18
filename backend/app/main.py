"""
Main FastAPI application for Revolution X
Ubuntu 24.04 optimized
"""

import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.database.connection import init_db, close_db
from app.api.v1.router import api_router

# Import connection managers
from app.mt5.connector import MT5ConnectionManager


# Global connection managers
mt5_manager = MT5ConnectionManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    Handles startup and shutdown events.
    """
    # Startup
    print(f"🚀 Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    
    # Initialize database
    await init_db()
    print("✅ Database initialized")
    
    # Initialize MT5 connection (optional in Phase 1)
    try:
        await mt5_manager.connect()
        print("✅ MT5 connected")
    except Exception as e:
        print(f"⚠️ MT5 not available: {e}")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down...")
    
    await mt5_manager.disconnect()
    await close_db()
    print("✅ Cleanup complete")


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered trading system for Gold and Metals",
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "operational",
        "environment": settings.ENVIRONMENT,
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for Docker."""
    health_status = {
        "status": "healthy",
        "database": "connected",  # TODO: Check actual connection
        "mt5": "connected" if mt5_manager.is_connected else "disconnected",
    }
    return health_status


@app.get("/info")
async def system_info():
    """System information endpoint."""
    import platform
    
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "environment": settings.ENVIRONMENT,
        "debug": settings.DEBUG,
        "tradable_assets": settings.TRADABLE_ASSETS,
    }


# WebSocket endpoint for real-time data
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """
    WebSocket endpoint for real-time updates.
    """
    await websocket.accept()
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            
            # Echo back for now (Phase 1)
            # TODO: Implement real-time market data in Phase 3
            await websocket.send_json({
                "type": "echo",
                "message": data,
                "status": "connected",
            })
            
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WebSocket error: {e}")
        await websocket.close()


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host=settings.BACKEND_HOST,
        port=settings.BACKEND_PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower(),
    )
