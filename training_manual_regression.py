from pycaret.regression import *

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
        
        metrics = pull()
        
        return predictions, metrics

# regresiones=["lr", "ridge", "lasso", "dt", "gbr", "rf", "en","br", "huber","lightgbm"]