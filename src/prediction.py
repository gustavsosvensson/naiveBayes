from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def prediction(stock_data):

    # Split the data into training and testing sets
    n=5
    X = stock_data[[f'Daily_Return_Lag_{lag}' for lag in range(1, n + 1)]]
    y = stock_data['Price_Increase']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Naive Bayes classifier
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    return y_pred, X_train, X_test, y_train, y_test