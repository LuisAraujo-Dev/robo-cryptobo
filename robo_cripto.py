import pandas as pd
import os 
import time

from binance.client import Client
from binance.enums import *

api_key = os.getenv("KEY_BINANCE")
secret_key = os.getenv("SECRET_BINANCE")

cliente_binance = Client(api_key, secret_key)