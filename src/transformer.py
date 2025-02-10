from src.coin import Coin
from src.util import ceil_3_decimals


def validate_data(data, required_fields):
    if not data:
        raise ValueError('Invalid data: None or empty')

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f'Missing Fields: {', '.join(missing_fields)}')


def transform(data):
    validate_data(data, ['symbol', 'name', 'market_data'])
    symbol = data['symbol']
    name = data['name']
    market_data = data['market_data']

    validate_data(market_data, ['current_price', 'market_cap', 'total_volume', 'total_supply', 'max_supply',
                                'circulating_supply', 'last_updated'])

    current_price = market_data['current_price']
    validate_data(current_price, ['usd'])
    current_price_usd = current_price.get('usd')

    market_cap = market_data['market_cap']
    validate_data(market_cap, ['usd'])
    market_cap_usd = market_cap.get('usd')

    total_volume = market_data['total_volume']
    validate_data(total_volume, ['usd'])
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

    return Coin(
        symbol=symbol,
        name=name,
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
