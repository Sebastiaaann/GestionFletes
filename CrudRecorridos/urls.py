from django.urls import path
from . import views

urlpatterns = [
   path('homeRecorridos/', views.homeRecorridos,name='homeRecorridos'),
   path('registrarRecorridos/', views.registrarRecorridos,name='registrarRecorridos'),
   path('editarRecorridos/<codigo>', views.editarRecorridos, name='editarRecorridos'),
   path('eliminarRecorridos/<codigo>', views.eliminarRecorridos, name='eliminarRecorridos'),
   path('edicionRecorridos/<codigo>', views.edicionRecorridos, name='edicionRecorridos'),
]
