from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registarVehiculo/', views.registarVehiculo),
    path('delVehiculo/<codigo>', views.delVehiculo, name="delVehiculo"),
    path('edicionVehiculo/<codigo>', views.edicionVehiculo, name="edicionVehiculo"),
    path('editarVehiculo/', views.editarVehiculo, name="editarVehiculo")
]