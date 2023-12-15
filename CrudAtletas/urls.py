from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AtletaViewSet, EventoViewSet

#http://127.0.0.1:8000/atletas/api/
#router = gestionar las rutas de las API y vincular a viewset

router = DefaultRouter()

# s registras los viewset 

router.register(r'atletasAPI', AtletaViewSet)
#http://localhost:8000/atletas/api/atletasAPI/

router.register(r'eventosAPI', EventoViewSet)
#http://localhost:8000/atletas/api/eventosAPI/

urlpatterns = [
    path('registrarAtleta/', views.registrarAtleta, name='registrarAtleta'),
    path('editarAtleta/<int:atletaID>/', views.editarAtleta, name='editarAtleta'),
    path('eliminarAtleta/<int:atletaID>/', views.eliminarAtleta, name='eliminarAtleta'),
    path('registrarEvento/', views.registrarEvento, name='registrarEvento'),
    path('editarEvento/<int:eventoID>/', views.editarEvento, name='editarEvento'),
    path('eliminarEvento/<int:eventoID>/', views.eliminarEvento, name='eliminarEvento'),
    path('exportar_pdf/', views.exportar_atletas_pdf, name='exportar_atletas_pdf'),
    path('exportar_excel/', views.exportar_atletas_excel, name='exportar_atletas_excel'),
    path('api/', include(router.urls)),
]