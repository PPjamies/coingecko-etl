from service import list_coins, get_coin_data_by_id


def etl():
    # get list of coins
    # coins {id, symbol, name, platforms: {}}
    coins = list_coins()

    # get coin data for each coin id == id
    # coin data {id, symbol, name, market_cap_rank, market_data:{}}
    # market_data: {current_price, market_cap: {}, total_volume: {}, price_change_24h, total_supply, max_supply, circulating_supply, last_updated }
    coin_data = []
    for coin in coins:
        coin_data.append(get_coin_data_by_id(coin.id))
