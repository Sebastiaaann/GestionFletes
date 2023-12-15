from django.shortcuts import render,redirect
from .models import Atleta, Evento
from .forms import AtletaForm, EventoForm
from django.contrib import messages
from django.http import HttpResponse
#PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
#EXCEL
from openpyxl import Workbook


def registrarAtleta(request):
    atletas = Atleta.objects.all()
    if request.method == 'POST':
        form = AtletaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atleta Registrado Correctamente!')
            return redirect('registrarAtleta')
        else:
            messages.error(request, 'Error al registrar el atleta. Por favor, verificar los datos.')
    else:
        form = AtletaForm()

    return render(request,'gestionAtletas.html', {"form":form, "atletas":atletas})

def editarAtleta(request, atletaID):
    atleta = Atleta.objects.get(atletaID=atletaID)
    if request.method == 'POST':
        form = AtletaForm(request.POST, instance=atleta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Atleta Editado Correctamente!')
            return redirect('registrarAtleta')
        else:
            messages.error(request, 'Error al editar el atleta. Por favor, verifica los datos.')
    else:
        form = AtletaForm(instance=atleta)

    return render(request, 'edicionAtletas.html', {'form':form,"atletaID":atletaID})

def eliminarAtleta(request, atletaID):
    atleta = Atleta.objects.get(atletaID=atletaID)
    atleta.delete()
    messages.success(request, 'Atleta Eliminado Correctamente!')
    return redirect('registrarAtleta')

# Evento 

def registrarEvento(request):
    eventos = Evento.objects.all()
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento Registrado Correctamente!')
            return redirect('registrarEvento')
        else:
            messages.error(request, 'Error al registrar el evento. Por favor, verificar los datos.')
    else:
        form = EventoForm()

    return render(request,'gestionEventos.html', {"form":form, "eventos":eventos})

def editarEvento(request, eventoID):
    evento = Evento.objects.get(id=eventoID)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento Editado Correctamente!')
            return redirect('registrarEvento')
        else:
            messages.error(request, 'Error al editar el evento. Por favor, verifica los datos.')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'edicionEventos.html', {'form':form,"eventoID":eventoID})

def eliminarEvento(request, eventoID):
    evento = Evento.objects.get(id=eventoID)
    evento.delete()
    messages.success(request, 'Evento Eliminado Correctamente!')
    return redirect('registrarEvento')


# PDF ATLETAS
def exportar_atletas_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="atletas.pdf"'

    p = canvas.Canvas(response, pagesize=landscape(letter))

    atletas = Atleta.objects.all()

    page_width, page_height = landscape(letter)
    x = 50
    y = page_height - 50
    lines_per_page = 30
    lines_drawn = 0

    for atleta in atletas:
        if lines_drawn == lines_per_page:
            p.showPage()
            y = page_height - 50
            lines_drawn = 0

        p.drawString(x, y, f"Nombre: {atleta.nombre}, Apellido: {atleta.apellido}, Disciplina: {atleta.disciplina}, Sexo: {atleta.sexo}, Preferencias: {atleta.preferencias_competencia}")
        y -= 20
        lines_drawn += 1

    p.showPage()
    p.save()

    return response


#EXCEL 

from django.http import HttpResponse
from openpyxl import Workbook

def exportar_atletas_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="atletas.xlsx"'

    wb = Workbook()
    ws = wb.active

    # Add header
    ws.append(['Nombre', 'Apellido', 'Disciplina', 'Sexo', 'Preferencias'])

    atletas = Atleta.objects.all()
    for atleta in atletas:
        ws.append([atleta.nombre, atleta.apellido, atleta.disciplina, atleta.sexo, atleta.preferencias_competencia])

    wb.save(response)

    return response

from rest_framework import viewsets,permissions
from .serializers import AtletaSerializer, EventoSerializer

#Los viewset se utilizan en las urls, s crea una ruta para poder consultar los datos
# viewsets proporciona una interfaz para interactuar con el modelo

class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    
    #queryset = conjunto de datos 
    #cuando se utilize el viewset vamos a consultar todos los objetos/datos del modelo atleta
    
    permission_classes = [
        permissions.AllowAny
    ]
    # cualquier cliente puede solicitar datos al servidor	
    
    serializer_class = AtletaSerializer
    # A partir d q serializer utiliza los datos para convertilos

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventoSerializer








