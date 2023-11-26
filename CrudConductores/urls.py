from django.urls import path
from . import views

urlpatterns = [
    path('HomeConductores', views.homeConductores, name="HomeConductores"),
    path('registrarConductor/', views.registrarConductor, name="RegistrarConductor"),
    path('eliminacionConductor/<rut>', views.eliminacionConductor, name="eliminacionConductor"),
    path('edicionConductor/<rut>', views.edicionConductor, name="edicionConductor"),
    path('editarConductor/"', views.editarConductor, name="editarConductor"),
]