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

# lista_1 = ('BTC', 'ETH', 'SOL')

# for asset in account["balances"]:
#     if float(asset["free"]) > 0:
    
#         print(asset)
        
# order = cliente_binance.create_order(
#     symbol = "SOLBRL",
#     side = SIDE_BUY, 
#     type = ORDER_TYPE_MARKET, 
#     quantity = 0.015
# )

# account = cliente_binance.get_account()

# lista_1 = ('BTC', 'ETH', 'SOL')

# for asset in account["balances"]:
#     if float(asset["free"]) > 0:
    
#         print(asset)


code_operated = "SOLBRL"
asset = "SOL"
candle_periode = Client.KLINE_INTERVAL_1HOUR
quantity = 0.015

def get_data(code, interval): 
    
    candles = cliente_binance.get_klines(symbol = code, interval = interval, limit = 1000)
    prices = pd.DataFrame(candles)
    prices.columns = ["open_time", "open", "max", "min", "closed", "bulk", "closed_time", "negociate_coins", "number_trades", "asset_bulk_base_buy", "asset_bulk_quotation", "-"]
    
    prices = prices[["closed", "closed_time"]]
    prices["closed_time"] = pd.to_datetime(prices["closed_time"], unit = "ms").dt.tz_localize("UTC")
    prices["closed_time"] = prices["closed_time"].dt.tz_convert("America/Sao_Paulo")
    
    print(prices)
    
get_data(code=code_operated, interval=candle_periode)

def strategy_trade(data, code_operated, quantity, atual_position):

    data["fast_mean"] = data["closed"].rolling(window=7).mean()
    data["low_mean"] = data["closed"].rolling(window=40).mean()

    last_fast_mean = data["fast_mean"].iloc[-1] 
    last_low_mean = data["low_mean"].iloc[-1]

    account = cliente_binance.get_account()

    lista_1 = ('BTC', 'ETH', 'SOL')

    for asset in account["balances"]:
    if asset["asset"] == code_operated:
    
        quantity = float(asset["free"])

    if last_fast_mean > last_low_mean:
        
        if atual_position == False:

            order = cliente_binance.create_order(
                symbol = code_operated,
                side = SIDE_BUY, 
                type = ORDER_TYPE_MARKET, 
                quantity = quantity
            )
            print("Comprou o ativo")
            atual_position = True
    
    elif last_fast_mean < last_low_mean: 

        if atual_position == True:

            order = cliente_binance.create_order(
                symbol = code_operated,
                side = SIDE_SELL, 
                type = ORDER_TYPE_MARKET, 
                quantity = int(atual_position)
            )
            print("Vendeu o ativo")
            atual_position = False