import pandas as pd
import yfinance as yf


def get_and_prepare_data(stock_symbol: str, start_date: str, end_date: str):
    # Define the stock symbol and download historical data using yfinance
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Calculate daily returns as a feature
    stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change().dropna()

    # Create a binary target variable for price increase (1) or decrease (0)
    stock_data['Price_Increase'] = (stock_data['Daily_Return'] > 0).astype(int)

    # Prepare features (lagged returns) and target variable
    n = 5  # Number of lags to consider
    for lag in range(1, n + 1):
        stock_data[f'Daily_Return_Lag_{lag}'] = stock_data['Daily_Return'].shift(lag)

    stock_data.dropna(inplace=True)

    return stock_data
