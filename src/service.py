import os

import requests
from dotenv import load_dotenv

load_dotenv()

domain = os.getenv('COINGECKO_DOMAIN')
api_key = os.getenv('COINGECKO_KEY')

if not domain:
    raise ValueError('Missing environment variable: COINGECKO_DOMAIN')
if not api_key:
    raise ValueError('Missing environment variable: COINGECKO_KEY')

headers = {
    'accept': 'application/json',
    'x_cg_demo_api_key': api_key
}


def list_coins():
    url = f'{domain}/coins/list'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
        return None


def fetch_coin_data_by_id(coin_id):
    url = f'{domain}/coins/{coin_id}'
    params = {
        'localization': 'false',
        'tickers': 'false',
        'community_data': 'false',
        'developer_data': 'false',
        'sparkline': 'false'
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error fetching data: {e}')
        return None
