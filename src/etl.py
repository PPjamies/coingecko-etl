import json

from src.coin import Coin, Session, create_coin
from src.service import fetch_coin_data_by_id
from src.util import ceil_3_decimals
from src.validator import validate


def extract():
    data = fetch_coin_data_by_id('bitcoin')
    return json.dumps(data)


def transform(data):
    """ Airflow casts results from extract_task into a json string """
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            return None

    validate(data, ['symbol', 'name', 'market_data'])
    symbol = data['symbol']
    coin_name = data['name']
    market_data = data['market_data']

    validate(market_data, ['current_price', 'market_cap', 'total_volume', 'total_supply', 'max_supply',
                           'circulating_supply', 'last_updated'])

    current_price = market_data['current_price']
    validate(current_price, ['usd'])
    current_price_usd = current_price.get('usd')

    market_cap = market_data['market_cap']
    validate(market_cap, ['usd'])
    market_cap_usd = market_cap.get('usd')

    total_volume = market_data['total_volume']
    validate(total_volume, ['usd'])
    total_volume_usd = total_volume.get('usd')

    total_supply = market_data['total_supply']
    max_supply = market_data['max_supply']
    circulating_supply = market_data['circulating_supply']
    last_updated = market_data['last_updated']

    # custom calculations
    unavailable_supply = ceil_3_decimals(
        (total_supply - circulating_supply)
        if total_supply is not None and circulating_supply is not None
        else None
    )

    issuance_progress = ceil_3_decimals(
        (total_supply / max_supply)
        if total_supply is not None and max_supply is not None and max_supply not in [None, 0]
        else None
    )

    coin = Coin(
        symbol=symbol,
        coin_name=coin_name,
        price=current_price_usd,
        market_cap=market_cap_usd,
        total_volume=total_volume_usd,
        total_supply=total_supply,
        max_supply=max_supply,
        circulating_supply=circulating_supply,
        unavailable_supply=unavailable_supply,
        issuance_progress=issuance_progress,
        updated_on=last_updated
    )
    return json.dumps(coin.to_dict())


def load(coin):
    if isinstance(coin, str):
        try:
            coin = json.loads(coin)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            return None

    with Session() as session:
        create_coin(session, Coin(**coin))
