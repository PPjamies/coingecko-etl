from coingecko.service.service import list_coins, fetch_coin_data_by_id


def transformer():
    # get list of coins
    try:
        coins = list_coins()

        # coin data {id, symbol, name, market_cap_rank, market_data:{}}
        # market_data: {current_price, market_cap: {}, total_volume: {}, price_change_24h, total_supply, max_supply, circulating_supply, last_updated }
        coin_data = []
        for coin in coins:
            coin_data = fetch_coin_data_by_id(coin.id)

            # create coin model

            # store coin into db

    except Exception as e:
        print("ERROR")
    finally:
        print("DO SOMETHING")
