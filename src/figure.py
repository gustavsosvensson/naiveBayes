from matplotlib import pyplot as plt


def plot_figure(y_test, y_pred):
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

    plt.figure(figsize=(10, 6))
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

    return plt.gcf(), plt.gcf(), plt.gcf()