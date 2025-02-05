import os
import unittest
from unittest.mock import patch

import requests
from dotenv import load_dotenv

load_dotenv()
domain = os.getenv('COINGECKO_DOMAIN')
if not domain:
    raise ValueError("Missing environment variable: COINGECKO_DOMAIN")


def list_coins():
    response = requests.get(f'{domain}/coins/list')
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_coin_data_by_id(coin_id):
    response = requests.get(f'{domain}/coins/{coin_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return []


class TestService(unittest.TestCase):
    @patch('requests.get')
    def test_list_coins(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "id": "bitcoin",
                "symbol": "btc",
                "name": "Bitcoin"
            },
            {
                "id": "ethereum",
                "symbol": "eth",
                "name": "Ethereum"
            }
        ]
        mock_get.return_value = mock_response

        coins = list_coins()
        assert coins

        for coin in coins:
            assert 'id' in coin
            assert 'symbol' in coin
            assert 'name' in coin

    @patch('requests.get')
    def test_fetch_coin_data_by_id(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
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
        mock_get.return_value = mock_response

        bitcoin = fetch_coin_data_by_id('bitcoin')
        assert bitcoin

        # check for values needed for model
        assert 'market_data' in bitcoin
        market_data = bitcoin['market_data']

        assert 'current_price' in market_data
        current_price = market_data['current_price']
        assert 'usd' in current_price

        assert 'market_cap' in market_data
        market_cap = market_data['market_cap']
        assert 'usd' in market_cap

        assert 'total_volume' in market_data
        total_volume = market_data['total_volume']
        assert 'usd' in total_volume

        assert 'total_supply' in market_data
        assert 'max_supply' in market_data
        assert 'circulating_supply' in market_data
        assert 'last_updated' in market_data
