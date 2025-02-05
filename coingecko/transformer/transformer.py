import pandas as pd

from coingecko.db.coin import Coin


def transform_data(data):
    df = pd.DataFrame.from_dict(data)
    # print(df)

    # extract columns
    df['price'] = ""

    # create custom columns
    df['issuance_progress'] = df['total_supply'] / df['max_supply']
    df['unavailable_supply'] = df['total_supply'] - df['circulating_supply']

    return Coin(
        symbol=df['symbol'],
        name=df['name'],
        price=df['price'],
        total_volume=df['total_volume'],
        total_supply="",
        max_supply="",
        market_cap="",
        issuance_progress=df['issuance_progress'],
        circulating_supply=df['circulating_supply'],
        unavailable_supply=df['unavailable_supply'],
        updated_on=df['last_updated']
    )
