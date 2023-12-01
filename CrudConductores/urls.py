from django.urls import path
from . import views

urlpatterns = [
    path('registrarConductores/', views.registrarConductores, name="registrarConductores"),
    path('editarConductores/<conductorID>', views.editarConductores, name="editarConductores"),
    path('eliminarConductores/<conductorID>', views.eliminarConductores, name="eliminarConductores"),
]