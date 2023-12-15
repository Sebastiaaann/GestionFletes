from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_rut(value):
    # verifica si el rut tiene un formato de rut 
    if not re.match(r'^\d{1,2}\.\d{3}\.\d{3}[-][0-9kK]{1}$', value):
        raise ValidationError(
            ('El rut : %(value)s no es un RUT valido. Debe tener el formato: XX.XXX.XXX-K'),
            params={'value': value},
        )

# Create your models here.
class Atleta(models.Model):
    SEXO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]

    

    atletaID = models.AutoField(primary_key=True)
    rut = models.CharField(unique= True, max_length=12, validators=[validate_rut], error_messages={
            'unique': " Ya existe un Usuario con este RUt.",
        })  
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    disciplina = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    preferencias_competencia = models.TextField()  

    def __str__(self):
        texto= "{0} "
        return texto.format( self.rut)

class Evento(models.Model):
    C_carreras = [
        ('1','100 metros'),
        ('2','Maraton'),
    ]

    C_saltos = [
        ('1','Salto de altura'),
        ('2','Salto de longitud'),
        ('3','Salto con pértiga'),
    ]

    C_lanzamiento = [
        ('1','Lanzamiento de peso'),
        ('2','Lanzamiento de disco'),
        ('3','Lanzamiento de martillo'),
        ('4','Lanzamiento de jabalina'),

    ]

    C_Pruebas_Combinadas = [
        ('Masculino','Decatlón'),
        ('Femenino','Heptatlón'),
    ]

    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)
    carrera = models.CharField(max_length=50, choices=C_carreras, blank=True)
    salto = models.CharField(max_length=50, choices=C_saltos, blank=True)
    lanzamiento = models.CharField(max_length=50, choices=C_lanzamiento, blank=True)
    prueba_combinada = models.CharField(max_length=50, choices=C_Pruebas_Combinadas, blank=True)
