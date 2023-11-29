from django.db import models

# Create your models here.
class Recorridos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    conductor = models.CharField(max_length=70)
    fecha = models.DateField()
    ruta = models.CharField(max_length=70)
    cargaTransportada = models.CharField(max_length=70)
    detalleRecorridos = models.TextField(max_length=70)


    def __str__(self):
        texto= "{0} {1} {2} {3} {4} {5}"
        return texto.format(self.codigo, self.conductor, self.fecha, self.ruta, self.cargaTransportada, self.detalleRecorridos)
    