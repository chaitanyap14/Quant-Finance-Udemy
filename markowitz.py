import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as optimization
from alpaca.data.historical import StockHistoricalDataClient as shd
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

stock_client = shd("PK5F1SNAL6CVPPRH0SUK", "I5qnRDVNKqYgKe9pOTUsBRSyxvQT4HSYqGrkigkc")
stocks = ['AAPL', 'WMT', 'TSLA', 'GOOG', 'GE', 'AMZN']

request_params = StockBarsRequest(
    symbol_or_symbols = stocks,
    timeframe = TimeFrame.Day,
    start = datetime(2021, 10, 14),
    end = datetime(2024, 10, 13)
)

def show_data(data):
    data.plot(figsize = (10, 5))
    plt.show()

bars = stock_client.get_stock_bars(request_params)
bars = bars.df
dataset = bars.close

show_data(dataset)
