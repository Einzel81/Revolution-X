"""
Configuration module for Revolution X
Ubuntu 24.04 compatible settings
"""

import os
from functools import lru_cache
from typing import List, Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    APP_NAME: str = "Revolution X"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    
    # Server
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    ALGORITHM: str = "HS256"
    
    # Database - TimescaleDB
    DATABASE_URL: str = "postgresql://revolution_x:password@localhost:5432/revolution_x_db"
    DB_POOL_SIZE: int = 20
    DB_MAX_OVERFLOW: int = 10
    
    # MetaTrader 5
    MT5_HOST: str = "localhost"
    MT5_PORT: int = 8222
    MT5_TIMEOUT: int = 30
    
    # Trading
    DEFAULT_TIMEFRAME: str = "M15"
    MAX_CONCURRENT_TRADES: int = 5
    MAX_DAILY_TRADES: int = 20
    RISK_PER_TRADE: float = 0.02  # 2%
    MAX_TOTAL_RISK: float = 0.10  # 10%
    
    # Assets to trade
    TRADABLE_ASSETS: List[str] = [
        "XAUUSD",
        "XAGUSD",
        "XPTUSD",
        "XPDUSD",
    ]
    
    # Telegram (Optional)
    TELEGRAM_BOT_TOKEN: Optional[str] = None
    TELEGRAM_CHAT_ID: Optional[str] = None
    TELEGRAM_ENABLED: bool = False
    
    # AI Guardian (Optional)
    OPENAI_API_KEY: Optional[str] = None
    GUARDIAN_ENABLED: bool = False
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"  # Allow extra env vars


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


settings = get_settings()
