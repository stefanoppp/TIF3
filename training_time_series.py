import pandas as pd
import numpy as np
from pycaret.time_series import *
from statsmodels.tsa.stattools import adfuller

def preprocess_data(file_path):
    data = pd.read_csv(file_path, parse_dates=True, index_col=0)
    price_data = data['precio']
    
    # Transformar los datos con el logaritmo natural
    log_data = np.log(price_data)
    
    # Verificar estacionariedad y diferenciar si es necesario
    if adfuller(log_data)[1] > 0.05:
        log_data = log_data.diff().dropna()
    
    return log_data, price_data

def main():
    file_path = 'datasettif.csv'
    preprocessed_data, original_data = preprocess_data(file_path)

    try:
        best_model = load_model("best_time_series_model")
    except:
        setup(data=preprocessed_data, fh=5, session_id=123)
        best_model = compare_models(sort='MAE')
        save_model(best_model, "best_time_series_model")
        plot_model(best_model, plot='forecast')

    # Realizar predicciones
    print(best_model)
    predictions = predict_model(best_model, fh=12)['y_pred']
    
    # Revertir las transformaciones a la escala original
    last_log_value = np.log(original_data.iloc[-1])
    predictions_log_scale = predictions.cumsum() + last_log_value
    predictions_orig_scale = np.exp(predictions_log_scale)
    
    return predictions_orig_scale

predictions=main()