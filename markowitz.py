import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from alpaca.data.historical import StockHistoricalDataClient as shd
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

#Data Collection
stock_client = shd("PK5F1SNAL6CVPPRH0SUK", "I5qnRDVNKqYgKe9pOTUsBRSyxvQT4HSYqGrkigkc")
stocks = ['AAPL', 'TSLA', 'GOOG', 'AMZN', 'META', 'BRK.B', 'JPM']

request_params = StockBarsRequest(
    symbol_or_symbols = stocks,
    timeframe = TimeFrame.Day,
    start = datetime(2022, 10, 14),
    end = datetime(2024, 10, 13)
)

def show_data(data):
    data.plot(figsize = (10, 5))
    plt.show()

def get_data():
    bars = stock_client.get_stock_bars(request_params)
    close_bars = pd.DataFrame(bars.df.close)
    close_bars = close_bars.reset_index().rename(columns = {'symbol': 'symbol', 'timestamp': 'timestamp'})
    dataset = close_bars.pivot(index = 'timestamp', columns = 'symbol', values = 'close')
    return dataset

#Dataset
dataset = get_data()
show_data(dataset)

#Model Implementation
TRADING_DAYS = 252
NUM_PORTFOLIOS = 10000

def log_return(data):
    log_return = np.log(data/data.shift(1))
    return log_return[1:]

def show_stats(data):
    print(data.mean()*TRADING_DAYS)
    print(data.cov()*TRADING_DAYS)

def show_mean_variance(returns, weights):
    portfolio_return = np.sum(returns.mean()*weights)*TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov()*TRADING_DAYS, weights)))
    print("Expected Portfolio Return: ", portfolio_return)
    print("Expected Portfolio Volatility: ", portfolio_volatility)

def portfolio_gen(returns):
    portfolio_returns = []
    portfolio_risk = []
    portfolio_weights = []

    for i in range(NUM_PORTFOLIOS):
        w = np.random.random(len(stocks))
        #Normalizing so sum is 1
        w /= np.sum(w)
        portfolio_weights.append(w)
        portfolio_returns.append(np.sum(returns.mean()*w)*TRADING_DAYS)
        portfolio_risk.append(np.sqrt(np.dot(w.T, np.dot(returns.cov()*TRADING_DAYS, w))))

    return np.array(portfolio_returns), np.array(portfolio_risk), np.array(portfolio_weights)


def show_portfolios(returns, risk):
    plt.figure(figsize=(10,6))
    plt.scatter(risk, returns, c=returns/risk, marker='o')
    plt.grid(True)
    plt.xlabel('Expected Risk')
    plt.ylabel('Expected Returns')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()

def print_optimal_portfolio(sr, r, v, w):
    optimal_index = np.where(sr == sr.max())
    print("Optimal Returns: ", r[optimal_index])
    print("Optimal Volatility: ", v[optimal_index])
    print("Optimal Sharpe Ratio: ", sr.max())
    print("Optimal Portfolio weights: ", w[optimal_index])

log_daily_returns = log_return(dataset)
show_stats(log_daily_returns)

returns, risk, weights = portfolio_gen(log_daily_returns)
show_portfolios(returns, risk)

print_optimal_portfolio(returns/risk, returns, risk, weights)
