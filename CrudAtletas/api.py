# from .models import Atleta, Evento
# from rest_framework import viewsets, permissions
# from .serializers import AtletaSerializer, EventoSerializer

# #Se ocupa con urls, s crea una ruta para poder consultar los datos

# class AtletaViewSet(viewsets.ModelViewSet):
#     queryset = Atleta.objects.all()
    
#     #queryset = conjunto de datos 
#     #cuando se utilize el viewset vamos a consultar todos los objetos/datos del modelo atleta
    
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     # cualquier cliente puede solicitar datos al servidor	
    
#     serializer_class = AtletaSerializer
#     # A partir d q serializer utiliza los datos

# class EventoViewSet(viewsets.ModelViewSet):
#     queryset = Evento.objects.all()
#      #cuando se utilize el viewset vamos a consultar todos los objetos/datos del modelo EvENTO
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = EventoSerializer