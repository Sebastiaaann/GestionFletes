from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mantenciones
from .forms import MantencionForm

def registrarMantenciones(request):
    mantenciones = Mantenciones.objects.all()
    if request.method == 'POST':
        form = MantencionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantencion Registrada Correctamente!')
            return redirect('registrarMantenciones')
        else:
            messages.error(request, 'Error al registrar la mantencion. Por favor, verificar los datos.')
            return render(request,'gestionMantenciones.html', {"form":form, "mantenciones":mantenciones})
    else:
        form = MantencionForm()
        return render(request,'gestionMantenciones.html', {"form":form, "mantenciones":mantenciones})

def editarMantenciones(request, mantencionID):
    mantencion = Mantenciones.objects.get(mantencionID=mantencionID)
    if request.method == 'POST':
        form = MantencionForm(request.POST, instance=mantencion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantencion Editada Correctamente!')
            return redirect('registrarMantenciones')
        else:
            messages.error(request, 'Error al editar la mantencion. Por favor, verifica los datos.')
            return render(request, 'edicionMantenciones.html', {'form':form,"mantencionID":mantencionID})
    else:
        form = MantencionForm(instance=mantencion)
        return render(request, 'edicionMantenciones.html', {'form':form,"mantencionID":mantencionID})

def eliminarMantenciones(request,mantencionID):
    mantencion = Mantenciones.objects.get(mantencionID=mantencionID)
    mantencion.delete()
    messages.success(request,'Mantencion Eliminada Correctamente!')
    return redirect('registrarMantenciones')