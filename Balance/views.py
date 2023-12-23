from django.shortcuts import render
from CrudVehiculos.models import Vehiculos

def balance(request):
    vehiculos_inactivos = Vehiculos.objects.filter(estado='inactivo').count()
    vehiculos_activos = Vehiculos.objects.filter(estado='activo').count()
    context = {
        'vehiculos_inactivos': vehiculos_inactivos,
        'vehiculos_activos': vehiculos_activos,
        }
    return render(request, 'Balance.html', context)
