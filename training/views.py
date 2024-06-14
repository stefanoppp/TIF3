from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from training_time_series import main

from training_manual_regression import RegressionModel
from training_manual_tseries import TimeSeries

from .forms import ModelSelectionForm

import plotly.graph_objects as go
import plotly.io as pio  # Elimina esta línea

import json
from plotly.utils import PlotlyJSONEncoder  # Importa la clase PlotlyJSONEncoder
import pandas as pd

def home(request):
    return render(request, "training/home.html")

@login_required
def train(request):
    return render(request, "training/train.html")

@login_required
def developer_mode(request):
    if request.method == 'POST':
        form = ModelSelectionForm(request.POST)
        if form.is_valid():
            model_select = form.cleaned_data['model_select']
            model_parameters = form.cleaned_data['model_parameters']
            test_percentage = form.cleaned_data['test_percentage']

            # Solo cargar los datos cuando se envía el formulario
            all_data = pd.read_csv('datasettif.csv')
            all_data['fecha'] = pd.to_datetime(all_data['fecha'])

            # Lógica para el entrenamiento del modelo basado en la selección del usuario
            if model_select == "regression":
                regresor_model = RegressionModel(all_data)
                train_percentage = 1 - test_percentage
                predictions, metrics = regresor_model.start_model(model_parameters, train_percentage)

            else:
                price_data = all_data['precio']
                t_series_model = TimeSeries(price_data)
                test_size = int(test_percentage * len(price_data))
                predictions, metrics = t_series_model.start_model(model_parameters, 10, test_size)

            # Generar el gráfico de predicciones
            # Renderizar la página de resultados con los datos obtenidos
            return render(request, "training/process_developer_mode.html", {
                'model_select': model_select,
                'model_parameters': model_parameters,
                'test_percentage': test_percentage,
                'metricas': metrics,
                'predictions': predictions,
            })
    else:
        form = ModelSelectionForm()
    
    return render(request, "training/developer_mode.html", {'form': form})



@login_required
def process_developer_mode(request):
    if request.method == 'POST':
        form = ModelSelectionForm(request.POST)
        if form.is_valid():
            model_select = form.cleaned_data['model_select']
            model_parameters = form.cleaned_data['model_parameters']
            test_percentage = form.cleaned_data['test_percentage']
            all_data = pd.read_csv('datasettif.csv')
            all_data['fecha'] = pd.to_datetime(all_data['fecha'])

            if model_select=="regression":
                regresor_model=RegressionModel(all_data)
                print("Procesando modelo...")
                train_percentage=1-test_percentage
                predictions, metrics=regresor_model.start_model(model_parameters, train_percentage)

            else:
                price_data = all_data['precio']
                t_series_model=TimeSeries(price_data)
                test_size=int(test_percentage*len(price_data))
                predictions, metrics=t_series_model.start_model(model_parameters, 10, test_size)

            return render(request, "training/process_developer_mode.html", {
                'model_select': model_select,
                'model_parameters': model_parameters,
                'test_percentage': test_percentage,
                'metricas': metrics,
                'predictions':predictions
            })
    return render(request, "training/developer_mode.html")


@login_required
def automatic_mode(request):
    predictions = main()  
    df_predictions = predictions.reset_index()
    df_predictions.columns = ['Periodo', 'Prediccion']
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_predictions['Periodo'],
        y=df_predictions['Prediccion'],
        mode='lines+markers',
        name='Predicción'
    ))

    fig.update_layout(
        title='Predicciones',
        xaxis_title='Perido a partir de Abril-2024',
        yaxis_title='Valor predicho',
        template='plotly_dark'
    )

    graph_div = pio.to_html(fig, full_html=False)

    return render(request, "training/automatic_mode.html", {'result': df_predictions.to_html(index=False), 'graph_div': graph_div})

def exit(request):
    logout(request)
    return redirect(home)