import pandas as pd

from src.get_data import get_and_prepare_data


def test_get_and_prepare_data():
    stock_data = get_and_prepare_data(stock_symbol="AAPL", start_date="2022-12-14", end_date="2023-12-14")

    # Assert that the stock_data is a DataFrame
    assert isinstance(stock_data, pd.DataFrame)

    # Assert that the DataFrame has columns 'Daily_Return' and 'Price_Increase'
    assert 'Daily_Return' in stock_data.columns
    assert 'Price_Increase' in stock_data.columns

    # Assert that there are no missing values in the DataFrame
    assert not stock_data.isnull().any().any()

    # Assert that 'Price_Increase' column only contains 0 or 1 values
    assert all((stock_data['Price_Increase'] == 0) | (stock_data['Price_Increase'] == 1))


