import requests

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_price(crypto="bitcoin", currency="usd"):
    params = {
        "ids": crypto.lower(),
        "vs_currencies": currency.lower()
    }
    
    response = requests.get(COINGECKO_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data.get(crypto, {}).get(currency, None)
    else:
        return None

# Fetch and store price in variable
crypto = "bitcoin"
currency = "usd"
crypto_price = get_crypto_price(crypto, currency)
crypto_per_dollar = 1 / crypto_price
print(crypto_per_dollar)
print(type(crypto_per_dollar))
