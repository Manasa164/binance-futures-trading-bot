# bot/client.py
from binance.client import Client
from dotenv import load_dotenv
import os, time

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Create client
client = Client(API_KEY, API_SECRET, testnet=True)

# Sync time with server
server_time = client.get_server_time()['serverTime']
local_time = int(time.time() * 1000)
client.TIME_OFFSET = server_time - local_time

def get_client():
    return client
