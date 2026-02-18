"""
MetaTrader 5 connector for Revolution X
ZeroMQ based communication
Ubuntu 24.04 compatible
"""

import asyncio
import json
import zmq
import zmq.asyncio
from typing import Optional, Dict, Any

from app.config import settings


class MT5ConnectionManager:
    """
    Manages connection to MetaTrader 5 via ZeroMQ.
    Handles order execution and market data.
    """
    
    def __init__(self):
        self.context: Optional[zmq.asyncio.Context] = None
        self.socket: Optional[zmq.asyncio.Socket] = None
        self.is_connected: bool = False
        self._lock = asyncio.Lock()
    
    async def connect(self) -> bool:
        """
        Establish connection to MT5 ZeroMQ server.
        """
        try:
            async with self._lock:
                if self.is_connected:
                    return True
                
                self.context = zmq.asyncio.Context()
                self.socket = self.context.socket(zmq.REQ)
                self.socket.setsockopt(zmq.RCVTIMEO, settings.MT5_TIMEOUT * 1000)
                self.socket.setsockopt(zmq.LINGER, 0)
                
                address = f"tcp://{settings.MT5_HOST}:{settings.MT5_PORT}"
                self.socket.connect(address)
                
                # Test connection
                await self._send_command({"action": "ping"})
                
                self.is_connected = True
                print(f"✅ Connected to MT5 at {address}")
                return True
                
        except Exception as e:
            print(f"❌ Failed to connect to MT5: {e}")
            self.is_connected = False
            return False
    
    async def disconnect(self):
        """Close connection."""
        async with self._lock:
            if self.socket:
                self.socket.close()
                self.socket = None
            if self.context:
                self.context.term()
                self.context = None
            self.is_connected = False
            print("🔌 Disconnected from MT5")
    
    async def _send_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send command to MT5 and receive response.
        """
        if not self.socket:
            raise ConnectionError("Not connected to MT5")
        
        try:
            # Send command
            await self.socket.send_json(command)
            
            # Receive response
            response = await self.socket.recv_json()
            return response
            
        except zmq.error.Again:
            raise TimeoutError("MT5 request timed out")
        except Exception as e:
            raise ConnectionError(f"MT5 communication error: {e}")
    
    async def get_account_info(self) -> Optional[Dict[str, Any]]:
        """
        Get MT5 account information.
        """
        if not self.is_connected:
            return None
        
        try:
            response = await self._send_command({"action": "account_info"})
            return response.get("data")
        except Exception as e:
            print(f"Error getting account info: {e}")
            return None
    
    async def get_symbol_info(self, symbol: str) -> Optional[Dict[str, Any]]:
        """
        Get symbol information.
        """
        if not self.is_connected:
            return None
        
        try:
            response = await self._send_command({
                "action": "symbol_info",
                "symbol": symbol,
            })
            return response.get("data")
        except Exception as e:
            print(f"Error getting symbol info: {e}")
            return None
    
    async def place_order(
        self,
        symbol: str,
        direction: str,
        volume: float,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None,
        comment: str = "Revolution X",
    ) -> Optional[Dict[str, Any]]:
        """
        Place a new order in MT5.
        """
        if not self.is_connected:
            raise ConnectionError("MT5 not connected")
        
        order_type = "ORDER_TYPE_BUY" if direction == "buy" else "ORDER_TYPE_SELL"
        
        command = {
            "action": "place_order",
            "symbol": symbol,
            "order_type": order_type,
            "volume": volume,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "comment": comment,
        }
        
        response = await self._send_command(command)
        return response
    
    async def close_position(self, ticket: int) -> Optional[Dict[str, Any]]:
        """
        Close an open position.
        """
        if not self.is_connected:
            raise ConnectionError("MT5 not connected")
        
        command = {
            "action": "close_position",
            "ticket": ticket,
        }
        
        response = await self._send_command(command)
        return response
    
    async def get_positions(self) -> list:
        """
        Get all open positions.
        """
        if not self.is_connected:
            return []
        
        try:
            response = await self._send_command({"action": "get_positions"})
            return response.get("data", [])
        except Exception as e:
            print(f"Error getting positions: {e}")
            return []
