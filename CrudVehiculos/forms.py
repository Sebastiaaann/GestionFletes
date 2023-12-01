from django import forms
from .models import Vehiculos

class VehiculosForm(forms.ModelForm):
    patente = forms.CharField(error_messages={'unique':'La patente ya existe'})
    fechaAdquisicion = forms.DateField(label='Fecha de Adquisicion')
    class Meta:
        model = Vehiculos
        fields = ['patente','marca','modelo','fechaAdquisicion','estado','comentario']