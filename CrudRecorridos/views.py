from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recorridos
from .forms import RecorridosForm
from django.contrib.auth.decorators import login_required


@login_required
def registrarRecorridos(request):
    recorridos = Recorridos.objects.all()
    if request.method == 'POST':
        form = RecorridosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recorrido Registrado Correctamente!')
            return redirect('registrarRecorridos')
        else:
            messages.error(request, 'Error al registrar el recorrido. Por favor, verificar los datos.')
            return render(request,'gestionRecorrido.html', {"form":form, "recorridos":recorridos})
    else:
        form = RecorridosForm()
        return render(request,'gestionRecorrido.html', {"form":form, "recorridos":recorridos})

def editarRecorridos(request, recorridoID):
    recorrido = Recorridos.objects.get(recorridoID=recorridoID)
    if request.method == 'POST':
        form = RecorridosForm(request.POST, instance=recorrido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recorrido Editado Correctamente!')
            return redirect('registrarRecorridos')
        else:
            messages.error(request, 'Error al editar el recorrido. Por favor, verifica los datos.')
            return render(request, 'edicionRecorrido.html', {'form':form,"recorridoID":recorridoID})
    else:
        form = RecorridosForm(instance=recorrido)
        return render(request, 'edicionRecorrido.html', {'form':form,"recorridoID":recorridoID})

def eliminarRecorridos(request,recorridoID):
    recorrido = Recorridos.objects.get(recorridoID=recorridoID)
    recorrido.delete()
    messages.success(request,'Recorrido Eliminado Correctamente!')
    return redirect('registrarRecorridos')

  
#Excel
from openpyxl import Workbook
from django.http import HttpResponse

def descargarRecorridos(request):
    recorridos = Recorridos.objects.all()
    wb = Workbook()
    ws = wb.active
    ws.append(['recorridoID', 'conductor', 'vehiculo.', 'fecha', 'direccionOrigen', 'direccionDestino', 'carga', 'detalle'])

    for recorrido in recorridos:
        ws.append([recorrido.recorridoID, recorrido.conductor.nombre, recorrido.vehiculo.patente, recorrido.fecha, recorrido.direccionOrigen, recorrido.direccionDestino, recorrido.carga, recorrido.detalle])
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="recorridos.xlsx"'
    wb.save(response)

    return response