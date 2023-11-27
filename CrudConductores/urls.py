from django.urls import path
from . import views

urlpatterns = [
    path('homeConductores/', views.homeConductores, name="homeConductores"),
    path('registrarConductor/', views.registrarConductor, name="registrarConductor"),
    path('eliminacionConductor/<rut>', views.eliminacionConductor, name="eliminacionConductor"),
    path('edicionConductor/<rut>', views.edicionConductor, name="edicionConductor"),
    path('editarConductor/"', views.editarConductor, name="editarConductor"),
]