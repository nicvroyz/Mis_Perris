from django.db import models
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

# Create your models here.

class Tipo_Vivienda(models.Model):
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

class Region(models.Model):
    numero_region = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return "Region " + str(self.numero_region) + ": " + self.descripcion

class Ciudad(models.Model):
    numero_ciudad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    numero_region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Usuario(models.Model):
    correo_electronico = models.EmailField(max_length=30)
    rut = models.SlugField(primary_key=True, max_length=10)    
    password = models.CharField(max_length=30)
    password_verification = models.CharField(max_length=30)
    nombre_completo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    tipo_vivienda = models.ForeignKey(Tipo_Vivienda, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut + " - " + self.nombre_completo

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()