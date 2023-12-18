from src.figure import figure


def test_figure(y_test, y_pred):
    figure1, figure2, figure3 = figure(y_test, y_pred)
