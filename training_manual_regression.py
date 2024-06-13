from pycaret.regression import *
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

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

# Leer los datos
all_data = pd.read_csv('datasettif.csv')
regresiones=["lr", "ridge", "lasso", "dt"]
# Definir el tamaño de prueba y entrenar el modelo de regresión
test_porcentage = 0.1

train_porcentage=1-test_porcentage

# Instanciar y entrenar el modelo de regresión lineal
model_regression = RegressionModel(all_data) 
predictions, metrics = model_regression.start_model("lasso", train_porcentage)

# Imprimir las predicciones y las métricas
print("Predicciones:")
print(predictions)
print("\nMétricas:")
print(metrics)
