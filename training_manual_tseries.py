from pycaret.time_series import *
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score

class TimeSeries:

    def __init__(self, data) -> None:
        self.data = data
    
    def start_model(self, modeltype, n_periodos, test_size):
        setup(self.data, fh=test_size, fold=1)  # Deshabilitar validación cruzada
        model_time_series = create_model(modeltype)
        predictions = predict_model(model_time_series, fh=n_periodos)

        # Obtener las predicciones del modelo
        predictions_df = predict_model(model_time_series)
        y_pred = predictions_df['y_pred']

        # Calcular el índice de inicio para y_true
        start_index = len(self.data) - test_size

        # Obtener los valores reales desde el DataFrame original a partir del índice de inicio
        y_true = self.data.iloc[start_index:]

        # Calcular las métricas
        mae = mean_absolute_error(y_true, y_pred)
        rmse = mean_squared_error(y_true, y_pred, squared=False)
        mape = mean_absolute_percentage_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)

        metrics = {
            'MAE': mae,
            'RMSE': rmse,
            'MAPE': mape,
            'R2': r2
        }

        return predictions, metrics

# time=["naive", "ets", "arima", "theta","tbats", "exp_smooth", "tbats"]

# all_data = pd.read_csv('datasettif.csv')
# all_data['fecha'] = pd.to_datetime(all_data['fecha'])
# price_data = all_data["precio"]
# t_series_model = TimeSeries(price_data)

# predictions, metrics = t_series_model.start_model("arima", 12, 4)
# print("\n")
# print(predictions)
# print("\n")
# print(metrics)