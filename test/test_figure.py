from src.figure import plot_figure


def test_figure(y_test, y_pred):
    figure1, figure2, figure3 = plot_figure(y_test, y_pred)
