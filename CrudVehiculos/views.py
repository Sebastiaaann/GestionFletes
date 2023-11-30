from django.shortcuts import render, redirect
from .models import Vehiculos
from .forms import VehiculosForm
from django.contrib import messages

def registarVehiculos(request):
    vehiculos = Vehiculos.objects.all()
    if request.method == 'POST':
        form = VehiculosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo Registrado Correctamente!')
            return redirect('registarVehiculos')
        else:
            messages.error(request, 'Error al registrar el vehiculo. Por favor, verificar los datos.')
            return render(request,'gestionVehiculos.html', {"form":form, "vehiculos":vehiculos})
    else:
        form = VehiculosForm()
        return render(request,'gestionVehiculos.html', {"form":form, "vehiculos":vehiculos})

def edicionVehiculos(request, vehiculoID):
    vehiculo = Vehiculos.objects.get(vehiculoID=vehiculoID)
    if request.method == 'POST':
        form = VehiculosForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo Editado Correctamente!')
            return redirect('registarVehiculos')
        else:
            messages.error(request, 'Error al editar el vehiculo. Por favor, verifica los datos.')
            return render(request, 'edicionVehiculos.html', {'form':form,"vehiculoID":vehiculoID})
    else:
        form = VehiculosForm(instance=vehiculo)
        return render(request, 'edicionVehiculos.html', {'form':form,"vehiculoID":vehiculoID})

def eliminarVehiculos(request, vehiculoID):
    vehiculo = Vehiculos.objects.get(vehiculoID=vehiculoID)
    vehiculo.delete()
    messages.success(request, 'Vehiculo Eliminado Correctamente!')
    return redirect('registarVehiculos')