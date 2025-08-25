import yfinance as yf 
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from stockdex import Ticker


def download_data(ticker: str, range: str, granularity: str):
    ticker = Ticker(ticker=ticker)
    price = ticker.yahoo_api_price(range=range, dataGranularity=granularity)
    return price 

def log_returns(price_data):
    return np.log(price_data[1:]/price_data[:-1])

