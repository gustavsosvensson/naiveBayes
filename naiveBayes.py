
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

from src.get_data import get_and_prepare_data
from src.prediction import prediction

# Get data
stock_data = get_and_prepare_data(stock_symbol="AAPL", start_date="2022-12-14", end_date="2023-11-14")

y_pred, X_train, X_test, y_train, y_test = prediction(stock_data)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Create a bar chart for actual outcomes
plt.figure(figsize=(10, 6))
plt.bar(range(len(y_test)), y_test, label='Actual Price Increase', color='blue', alpha=0.7)
plt.title('Actual Price Increase')
plt.xlabel('Sample Index')
plt.ylabel('Price Increase (1: Increase, 0: Decrease)')
plt.legend()
plt.show()

# Create a bar chart for predicted outcomes
plt.figure(figsize=(10, 6))
plt.bar(range(len(y_test)), y_pred, label='Predicted Price Increase', color='red', alpha=0.7)
plt.title('Predicted Price Increase')
plt.xlabel('Sample Index')
plt.ylabel('Price Increase (1: Increase, 0: Decrease)')
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
for i in range(len(y_test)):
    if y_test.iloc[i] == y_pred[i] or ((y_test[i] == 0) and y_pred[i] == 0):
        plt.bar(i, y_pred[i], label='Correct Prediction', color='green', alpha=0.7)
    else:
        plt.bar(i, 1, label='False Prediction', color='red', alpha=0.7)
plt.title('Predicted Price correction')
plt.xlabel('Sample Index')
plt.ylabel('Price Increase (1: Increase, 0: Decrease)')
plt.legend()
plt.show()