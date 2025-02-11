import datetime

from src.coin import Coin, create_coin, retrieve_coin, list_coins_by_symbol


def test_create_coin(session):
    coin = Coin(
        symbol='btc',
        coin_name='bitcoin',
        price=123.45,
        total_volume=123,
        total_supply=123,
        max_supply=123,
        market_cap=123.45,
        issuance_progress=0.123,
        circulating_supply=123,
        unavailable_supply=123,
        updated_on=datetime.datetime.now()
    )
    create_coin(session, coin)

    coins = list_coins_by_symbol(session, coin.symbol)
    assert len(coins) == 1

    expected_coin = coins[0]
    assert hasattr(expected_coin, 'id')

    actual_coin = retrieve_coin(session, expected_coin.id)
    assert expected_coin is actual_coin
