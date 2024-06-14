from django import forms

class ModelSelectionForm(forms.Form):
    MODEL_CHOICES = [
        ('regression', 'Regresión'),
        ('timeSeries', 'Series Temporales'),
    ]

    model_select = forms.ChoiceField(choices=MODEL_CHOICES, required=True, label='Técnica de aprendizaje')
    model_parameters = forms.CharField(required=True, label='Parámetros del Modelo')
    test_percentage = forms.FloatField(min_value=0, max_value=1, required=True, label='Porcentaje de Test')

    def __init__(self, *args, **kwargs):
        super(ModelSelectionForm, self).__init__(*args, **kwargs)
        self.fields['model_select'].widget.attrs.update({'class': 'form-control'})
        self.fields['model_parameters'].widget.attrs.update({'class': 'form-control'})
        self.fields['test_percentage'].widget.attrs.update({'class': 'form-control', 'step': '0.01'})

    def clean_test_percentage(self):
        data = self.cleaned_data['test_percentage']
        if self.cleaned_data['model_select'] == 'regression' and (data < 0.05 or data > 0.5):
            raise forms.ValidationError("Para regresión, el porcentaje de test debe estar entre 0.05 y 0.5.")
        if self.cleaned_data['model_select'] == 'timeSeries' and data > 0.25:
            raise forms.ValidationError("Para series temporales, el porcentaje de test debe estar entre 0 y 0.25.")
        return data
