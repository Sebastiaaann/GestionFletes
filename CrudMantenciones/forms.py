from django import forms
from django.forms.widgets import DateInput
from .models import Mantenciones
from datetime import date

class MantencionForm(forms.ModelForm):
    class Meta:
        model = Mantenciones
        fields = ['vehiculo','fechaInicio','duracion','valor']
    
    def __init__(self, *args, **kwargs):
        super(MantencionForm, self).__init__(*args, **kwargs)
        self.fields['fechaInicio'].widget = DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        self.fields['fechaInicio'].widget.attrs['min'] = '2000-01-01'
        self.fields['fechaInicio'].widget.attrs['max'] = str(date.today())