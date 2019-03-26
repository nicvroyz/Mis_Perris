from django.db import models
from Usuario.models import Usuario

# Create your models here.

class Estado(models.Model):
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

class Mascota(models.Model):    
    nombre = models.CharField(max_length=30)
    fotografia = models.ImageField(default='img_folder/None/no-img.jpg')
    raza = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

