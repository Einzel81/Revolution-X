#!/bin/bash
set -e

# Initialize TimescaleDB for Revolution X
# Run automatically on first container start

echo "Initializing Revolution X database..."

# Create extensions
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Enable TimescaleDB extension
    CREATE EXTENSION IF NOT EXISTS timescaledb;
    
    -- Enable UUID extension
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    
    -- Create schema if not exists
    CREATE SCHEMA IF NOT EXISTS trading;
    
    -- Grant permissions
    GRANT ALL PRIVILEGES ON SCHEMA trading TO $POSTGRES_USER;
    
    -- Set timezone
    SET timezone = 'UTC';
    
    -- Optimize for time-series data
    ALTER SYSTEM SET shared_preload_libraries = 'timescaledb';
    
    -- Create hypertable for market data (will be done by app)
    -- This is just initialization
    
    echo "Database initialization complete!";
EOSQL

echo "TimescaleDB ready for Revolution X!"
