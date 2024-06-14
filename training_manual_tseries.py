from pycaret.time_series import *

class TimeSeries:

    def __init__(self, data) -> None:
        self.data=data
    
    def start_model(self, modeltype, n_periodos, test_size):
        setup(self.data, fh=test_size)
        model_time_series=create_model(modeltype)
        predictions=predict_model(model_time_series, fh=n_periodos)

        metrics=pull()
        
        return predictions, metrics

# time=["naive", "ets", "arima", "theta","tbats", "exp_smooth", "tbats"]
