from binance.spot import Spot
import os
from dotenv import load_dotenv
load_dotenv()

client = Spot()

# Access testnet
#client = Spot(base_url='https://testnet.binance.vision')
#print(client.base_url)

# Get server timestamp
print(client.time())

# Get klines of BTCUSDT at 1m interval
#print(client.klines("BTCUSDT", "1m"))

# Get last 10 klines of BNBUSDT at 1h interval
#print(client.klines("BNBUSDT", "1h", limit=10))

# API key/secret are required for user data endpoints

# client testnet
# client = Spot(api_key=os.getenv('API_KEY_TESTNET'), api_secret=os.getenv('API_SECRET_TESTNET'))

# Account tesnet
# client = Spot(api_key=os.getenv('API_KEY_TESTNET_ACCOUNT'), api_secret=os.getenv('API_SECRET_TESTNET_ACCOUNT'))

# Vrai client Binance avec restriction IP: curl ifconfig.me
client = Spot(api_key=os.getenv('API_KEY'), api_secret=os.getenv('API_SECRET'))

# Get account and balance information

print(client.account())

# Post a new order
# params = {
#     'symbol': 'BTCUSDT',
#     'side': 'SELL',
#     'type': 'LIMIT',
#     'timeInForce': 'GTC',
#     'quantity': 0.002,
#     'price': 9500
# }

# response = client.new_order(**params)
#print(response)