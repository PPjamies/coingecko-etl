import json

from src.coin import Coin
from src.etl import transform


def test_transform():
    coin = Coin(
        symbol='btc',
        coin_name='Bitcoin',
        price=96875,
        total_volume=41434491297,
        total_supply=19820162,
        max_supply=21000000,
        market_cap=1918118941461,
        issuance_progress=0.944,
        circulating_supply=19820162,
        unavailable_supply=0,
    )

    data = {
        "id": "bitcoin",
        "symbol": "btc",
        "name": "Bitcoin",
        "market_data": {
            "current_price": {
                "usd": 96875,
                "vef": 9700.14,
                "vnd": 2438654711
            },
            "market_cap": {
                "usd": 1918118941461,
                "vef": 192061249609,
                "vnd": 48284994406866424
            },
            "total_volume": {
                "usd": 41434491297,
                "vef": 4148835614,
                "vnd": 1043034473673477,
            },
            "total_supply": 19820162,
            "max_supply": 21000000,
            "max_supply_infinite": False,
            "circulating_supply": 19820162,
            "last_updated": "2025-02-05T22:11:41.470Z"
        },
        "last_updated": "2025-02-05T22:11:41.470Z"
    }

    transformed_coin = transform(json.dumps(data))
    transformed_coin = json.loads(transformed_coin)
    assert transformed_coin
    assert transformed_coin["symbol"] == coin.symbol
    assert transformed_coin["coin_name"] == coin.coin_name
    assert transformed_coin["price"] == coin.price
    assert transformed_coin["total_volume"] == coin.total_volume
    assert transformed_coin["total_supply"] == coin.total_supply
    assert transformed_coin["max_supply"] == coin.max_supply
    assert transformed_coin["market_cap"] == coin.market_cap
    assert transformed_coin["issuance_progress"] == coin.issuance_progress
    assert transformed_coin["circulating_supply"] == coin.circulating_supply
    assert transformed_coin["unavailable_supply"] == coin.unavailable_supply
