from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recorridos

# Create your views here.
def registrarRecorridos(request):
    codigo = request.POST['codigoInput']
    conductor = request.POST['conductorInput']
    fecha = request.POST['fechaInput']
    ruta = request.POST['rutaInput']
    cargaTransportada = request.POST['cargaTransportadaInput']
    detalleRecorridos = request.POST['detallesRecorridoInput']
    recorrido = Recorridos.objects.create(
        codigo=codigo, conductor=conductor, fecha=fecha, ruta=ruta, cargaTransportada=cargaTransportada, detalleRecorridos=detalleRecorridos)
    messages.success(request,'Recorrido ingresado Correctamente')
    return redirect('homeRecorridos')

#listar recorridos
def homeRecorridos(request):
    recorrido = Recorridos.objects.all()
    return render (request, "gestionRecorrido.html",{"recorrido": recorrido})

def edicionRecorridos(request,codigo):
    recorrido = Recorridos.objects.get(codigo=codigo)
    return render(request, "edicionRecorrido.html", {"recorrido": recorrido})

#editar recorridos
def editarRecorridos(request):
    
    codigo = request.POST['codigoInput']
    conductor = request.POST['conductorInput']
    fecha = request.POST['fechaInput']
    ruta = request.POST['rutaInput']
    cargaTransportada = request.POST['cargaTransportadaInput']
    detallesRecorridos = request.POST['detallesRecorridosInput']
    
    recorrido = Recorridos.objects.get(codigo=codigo)

    recorrido.codigo = codigo
    recorrido.conductor = conductor
    recorrido.fecha = fecha
    recorrido.ruta = ruta
    recorrido.cargaTransportada = cargaTransportada
    recorrido.detalleRecorridos = detallesRecorridos
    recorrido.save()
    
    messages.success(request, 'Recorrido editado Correctamente')
    
    return redirect('homeRecorridos')


#eliminar recorridos
def eliminarRecorridos(request, codigo):
    recorrido = Recorridos.objects.get(codigo=codigo)
    recorrido.delete()
    messages.success(request, 'Recorrido eliminado exitosamente!')
    return redirect('homeRecorridos')
  
