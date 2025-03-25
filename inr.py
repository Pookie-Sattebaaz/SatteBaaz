import requests

EXCHANGE_RATE_API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_usd_to_inr():
    params = {
        "ids": "usd",
        "vs_currencies": "inr"
    }
    
    response = requests.get(EXCHANGE_RATE_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        inr_price = data.get("usd", {}).get("inr", None)
        return inr_price
    else:
        return None

# Fetch USD to INR exchange rate
usd_to_inr = get_usd_to_inr()

print(type(usd_to_inr))
print(usd_to_inr)
