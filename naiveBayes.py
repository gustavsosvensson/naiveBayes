import mplfinance
from matplotlib import pyplot as plt
from matplotlib.pyplot import axes
from sklearn.metrics import accuracy_score
from src.get_data import get_and_prepare_data
from src.figure import plot_figure
from src.prediction import prediction
import mplfinance as mpf

# This is a stock predictive model using the Gaussian Naive Bayes Classifiers,
# thus it generates a prediction of the stock, whether it increases or decreases (1 for the former, 0 for the latter).
# The model genertes its results from the stocks rate of return (RoR), a predicted High Yield would produce a 1, if not a 0
# Lastly the model produces a Mean Square error (MSE), representing the models accuracy during the specified testing period.
# MSE tracks the discrepancy between model results and the actual result (AR/PR), the goal being 1 (100%)

# Possible addiotns to the features:
# EPS
# Net assets per share
# Capital reserve per share
# Roe
# Operating Profit Ratio
# ROA
# Debt Asset ratio
# total asset turnover
# NEt assets Growth Rate
# ROIC

# Alternative action can be to add the accuracy for increasing stock and respectively decreasing value. 
stock_data = get_and_prepare_data(stock_symbol="NVDA", start_date="2022-12-14", end_date="2023-11-14")

y_pred, X_train, X_test, y_train, y_test = prediction(stock_data)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Create a bar chart for actual outcomes
figure1, figure2, figure3 = plot_figure(y_test, y_pred)

# ... (Your existing code for data preprocessing and model training)

plt.figure(figsize=(12, 6))
plt.plot(stock_data['Adj Close'], label='Stock Price', color='blue')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Stock Price Progression')
plt.legend()
plt.grid(True)