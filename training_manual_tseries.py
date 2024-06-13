from pycaret.time_series import *
import pandas as pd

class TimeSeries:

    def __init__(self, data) -> None:
        self.data=data
    
    def start_model(self, modeltype, n_periodos, test_size):
        setup(price_data, fh=test_size)
        model_time_series=create_model(modeltype)
        predictions=predict_model(model_time_series, fh=n_periodos)

        metrics=pull()
        
        return predictions, metrics
all_data = pd.read_csv('datasettif.csv')
price_data = all_data['precio']

time=["naive", "ets", "arima", "theta","tbats", "exp_smooth", "tbats"]

test_porcentage=0

periodos=15

test_size=int(len(price_data)*test_porcentage)
if test_size<1:
    test_size=1
model_time_series=TimeSeries(price_data) 
print(model_time_series.start_model("tbats",periodos,test_size))
