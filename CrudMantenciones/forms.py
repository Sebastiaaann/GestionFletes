from django import forms
from .models import Mantenciones

class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantenciones
        fields = ['codigo', 'vehiculo', 'fecha', 'valor']