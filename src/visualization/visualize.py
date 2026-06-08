import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#class Visualize:

def evaluate_model(y_test, y_pred_test):
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred_test)
    mae = mean_absolute_error(y_test, y_pred_test)

    r2 = r2_score(y_test, y_pred_test)

    return mse, mae, r2

def print_results(mse, mae, r2, y_test, y_pred_test, print_plot = False):
    # Print accuracy metrics
    print(f"Train MSE: {mse:.2f}")
    print(f"Test MAE: {mae:.2f}")
    print(f"R2 Score: {r2}")

    # Print plot
    if print_plot:
        plt.scatter(x = y_test, y = y_pred_test, color = "b")
        plt.xlabel("Real Values")
        plt.ylabel("Estimated Values")
        plt.title(f"Linear Regression Model With R2 Score of {r2}")
        plt.show()