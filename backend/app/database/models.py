"""
Database models for Revolution X
TimescaleDB optimized schema
"""

import uuid
from datetime import datetime
from decimal import Decimal
from enum import Enum

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.connection import Base


class UserRole(str, Enum):
    """User roles."""
    ADMIN = "admin"
    MANAGER = "manager"
    TRADER = "trader"
    VIEWER = "viewer"


class TradeStatus(str, Enum):
    """Trade statuses."""
    PENDING = "pending"
    OPEN = "open"
    CLOSED = "closed"
    CANCELLED = "cancelled"


class TradeDirection(str, Enum):
    """Trade directions."""
    BUY = "buy"
    SELL = "sell"


# ==========================================
# User Management Models (Phase 2)
# ==========================================

class User(Base):
    """User model."""
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False)
    role = Column(SQLEnum(UserRole), default=UserRole.TRADER, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    two_factor_enabled = Column(Boolean, default=False, nullable=False)
    two_factor_secret = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    trades = relationship("Trade", back_populates="user")
    sessions = relationship("UserSession", back_populates="user")
    
    __table_args__ = (
        Index("ix_users_email_active", "email", "is_active"),
    )


class UserSession(Base):
    """User session model."""
    __tablename__ = "user_sessions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    token = Column(Text, nullable=False)
    ip_address = Column(String(45), nullable=True)  # IPv6 compatible
    user_agent = Column(Text, nullable=True)
    is_revoked = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="sessions")
    
    __table_args__ = (
        Index("ix_sessions_user_id", "user_id"),
        Index("ix_sessions_token", "token"),
    )


class AuditLog(Base):
    """Audit log model."""
    __tablename__ = "audit_logs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    action = Column(String(100), nullable=False, index=True)
    details = Column(Text, nullable=True)  # JSON as text
    ip_address = Column(String(45), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    __table_args__ = (
        Index("ix_audit_user_id", "user_id"),
        Index("ix_audit_action_time", "action", "created_at"),
    )


# ==========================================
# Trading Models (Phase 3)
# ==========================================

class Trade(Base):
    """Trade model."""
    __tablename__ = "trades"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    
    # Trade details
    symbol = Column(String(20), nullable=False, index=True)
    direction = Column(SQLEnum(TradeDirection), nullable=False)
    status = Column(SQLEnum(TradeStatus), default=TradeStatus.PENDING, nullable=False)
    
    # Prices
    entry_price = Column(Numeric(15, 5), nullable=True)
    exit_price = Column(Numeric(15, 5), nullable=True)
    stop_loss = Column(Numeric(15, 5), nullable=True)
    take_profit = Column(Numeric(15, 5), nullable=True)
    
    # Position sizing
    volume = Column(Numeric(10, 2), nullable=False)
    risk_amount = Column(Numeric(15, 2), nullable=True)
    
    # Results
    profit_loss = Column(Numeric(15, 2), nullable=True)
    profit_loss_pips = Column(Numeric(10, 1), nullable=True)
    profit_loss_percent = Column(Numeric(8, 4), nullable=True)
    
    # AI & Strategy
    strategy = Column(String(50), nullable=True)
    ai_confidence = Column(Numeric(5, 2), nullable=True)  # 0-100
    entry_reason = Column(Text, nullable=True)
    
    # Timestamps
    opened_at = Column(DateTime(timezone=True), nullable=True)
    closed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="trades")
    
    __table_args__ = (
        Index("ix_trades_user_id", "user_id"),
        Index("ix_trades_symbol_status", "symbol", "status"),
        Index("ix_trades_created_at", "created_at"),
    )


# ==========================================
# Market Data Models (Phase 3)
# ==========================================

class MarketData(Base):
    """
    Market data model - TimescaleDB hypertable.
    Optimized for time-series data.
    """
    __tablename__ = "market_data"
    
    time = Column(DateTime(timezone=True), primary_key=True)
    symbol = Column(String(20), primary_key=True)
    timeframe = Column(String(10), primary_key=True)  # M15, H1, etc.
    
    # OHLCV
    open = Column(Numeric(15, 5), nullable=False)
    high = Column(Numeric(15, 5), nullable=False)
    low = Column(Numeric(15, 5), nullable=False)
    close = Column(Numeric(15, 5), nullable=False)
    volume = Column(BigInteger, nullable=False)
    
    # Additional data
    spread = Column(Numeric(10, 5), nullable=True)
    
    __table_args__ = (
        Index("ix_market_data_symbol_time", "symbol", "time"),
    )


# ==========================================
# System Models
# ==========================================

class SystemConfig(Base):
    """System configuration model."""
    __tablename__ = "system_config"
    
    id = Column(Integer, primary_key=True)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    updated_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)


class GuardianLog(Base):
    """AI Guardian activity log."""
    __tablename__ = "guardian_logs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    action_type = Column(String(50), nullable=False)  # fix, suggest, deploy
    description = Column(Text, nullable=False)
    old_value = Column(Text, nullable=True)
    new_value = Column(Text, nullable=True)
    applied = Column(Boolean, default=False)
    applied_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
