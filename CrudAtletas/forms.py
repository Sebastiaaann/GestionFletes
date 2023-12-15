from django import forms
from .models import Atleta, Evento

class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = '__all__'

class EventoForm(forms.ModelForm):
    rut = forms.ModelChoiceField(queryset=Atleta.objects.all())

    class Meta:
        model = Evento
        fields = '__all__'