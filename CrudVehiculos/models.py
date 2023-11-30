from django.db import models


class Vehiculos(models.Model):
    vehiculoID = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=50)
    fechaAdquisicion = models.DateField()
    estado = models.CharField(max_length=10, choices=[('activo', 'Activo'),('inactivo', 'Inactivo'),], default='activo')
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        texto= "{0} {1} {2} {3} {4} {5} {6}"
        return texto.format(self.vehiculoID, self.patente, self.marca, self.modelo, self.fechaAdquisicion, self.estado, self.comentarios)