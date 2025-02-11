CREATE TABLE IF NOT EXISTS coins (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(5) NOT NULL,
    coin_name VARCHAR(30) NOT NULL,
    price DOUBLE PRECISION,
    total_volume BIGINT,
    total_supply BIGINT,
    max_supply BIGINT,
    market_cap DOUBLE PRECISION,
    issuance_progress DOUBLE PRECISION,
    circulating_supply BIGINT,
    unavailable_supply BIGINT,
    updated_on TIMESTAMP
);