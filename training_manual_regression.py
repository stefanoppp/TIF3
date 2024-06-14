from pycaret.regression import *
from pycaret.datasets import get_data
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error

class RegressionModel:
    def __init__(self, data) -> None:
        self.data = data
    
    def start_model(self, modeltype, train_porcentage):
        # Configurar el entorno de PyCaret para regresión
        setup(data=self.data, target='precio', train_size=train_porcentage, session_id=123)
        
        # Crear y entrenar el modelo
        model_regression = create_model(modeltype)
        
        # Realizar predicciones en el conjunto de prueba
        predictions = predict_model(model_regression)
        
        # Calcular métricas por separado
        mae = mean_absolute_error(predictions['precio'], predictions['prediction_label'])
        rmse = mean_squared_error(predictions['precio'], predictions['prediction_label'], squared=False)
        mape = mean_absolute_percentage_error(predictions['precio'], predictions['prediction_label'])
        r2 = r2_score(predictions['precio'], predictions['prediction_label'])
        
        metrics = {
            'MAE': mae,
            'RMSE': rmse,
            'MAPE': mape,
            'R2': r2
        }
        
        return predictions, metrics

# Para probar la clase

# data = get_data("datasettif")
# model = RegressionModel(data)
# predictions, metrics = model.start_model("lr", 0.8)
# print("Metrics:")
# print(metrics)

# regresiones=["lr", "ridge", "lasso", "dt", "gbr", "rf", "en","br", "huber","lightgbm"]