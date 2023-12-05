from django import forms
from .models import Recorridos

class RecorridosForm(forms.ModelForm):
    class Meta:
        model = Recorridos
        fields = ['conductor','vehiculo','fecha','cargaTransportada','rutaRecorrido','ganancia','gasto']
