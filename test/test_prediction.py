import pandas as pd

from src.get_data import get_and_prepare_data
from src.prediction import prediction

stock_data = get_and_prepare_data(stock_symbol="AAPL", start_date="2022-12-14", end_date="2023-12-14")
def test_prediction():
    y_pred = prediction(stock_data)