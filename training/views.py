from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from training_time_series import main
import plotly.graph_objects as go
import plotly.io as pio

def home(request):
    return render(request, "training/home.html")

@login_required
def train(request):
    return render(request, "training/train.html")

@login_required
def developer_mode(request):
    if request.method == 'POST':
        model_select = request.POST.get('modelSelect')
        model_parameters = request.POST.getlist('modelParameters')
        test_percentage = request.POST.get('testPercentage')
        return render(request, "training/process_developer_mode.html", {
            'model_select': model_select,
            'model_parameters': model_parameters,
            'test_percentage': test_percentage
        })
    return render(request, "training/developer_mode.html")

@login_required
def process_developer_mode(request):
    if request.method == 'POST':
        model_select = request.POST.get('modelSelect')
        model_parameters = request.POST.getlist('modelParameters')
        test_percentage = request.POST.get('testPercentage')
        result = f"Modelo: {model_select}, Parámetros: {model_parameters}, Porcentaje de prueba: {test_percentage}"
        return render(request, "training/process_developer_mode.html", {
            'result': result
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

    # Añadir título y etiquetas
    fig.update_layout(
        title='Predicciones',
        xaxis_title='Perido a partir de Abril-2024',
        yaxis_title='Valor predicho',
        template='plotly_dark'
    )

    # Convertir el gráfico a HTML
    graph_div = pio.to_html(fig, full_html=False)

    return render(request, "training/automatic_mode.html", {'result': df_predictions.to_html(index=False), 'graph_div': graph_div})

def exit(request):
    logout(request)
    return redirect(home)