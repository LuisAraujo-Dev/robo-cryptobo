import pandas as pd
import os
import time
from dotenv import load_dotenv
from binance.client import Client
from binance.enums import *

load_dotenv()

api_key = os.getenv("KEY_BINANCE")
secret_key = os.getenv("SECRET_BINANCE")

cliente_binance = Client(api_key, secret_key)

account = cliente_binance.get_account()

lista_1 = ('BTC', 'ETH', 'SOL')

for asset in account["balances"]:
    if float(asset["free"]) > 0:
    
        print(asset)
        
order = cliente_binance.create_order(
    symbol = "SOLBRL",
    side = SIDE_BUY, 
    type = ORDER_TYPE_MARKET, 
    quantity = 0.015
)

account = cliente_binance.get_account()

lista_1 = ('BTC', 'ETH', 'SOL')

for asset in account["balances"]:
    if float(asset["free"]) > 0:
    
        print(asset)