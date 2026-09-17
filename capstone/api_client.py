import requests


def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1,
        "sparkline": False,
    }
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(
            url, params=params, headers=headers, timeout=5
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[Warning] Live API call failed ({e}). Using mock data instead.")
        # Fallback dataset so the report always generates
        return [
            {
                "name": "Bitcoin",
                "current_price": 65000,
                "price_change_percentage_24h": 2.5,
                "market_cap": 1280000000000,
            },
            {
                "name": "Ethereum",
                "current_price": 3500,
                "price_change_percentage_24h": -1.2,
                "market_cap": 420000000000,
            },
            {
                "name": "Tether",
                "current_price": 1.0,
                "price_change_percentage_24h": 0.01,
                "market_cap": 110000000000,
            },
            {
                "name": "BNB",
                "current_price": 580,
                "price_change_percentage_24h": 0.8,
                "market_cap": 85000000000,
            },
            {
                "name": "Solana",
                "current_price": 145,
                "price_change_percentage_24h": 4.1,
                "market_cap": 68000000000,
            },
        ]