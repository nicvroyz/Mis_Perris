from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from Mascotas.models import Estado, Mascota


# Create your views here.
def index(request):
    try:
        estado = Estado.objects.get(descripcion='Disponible')
        disponibles = Mascota.objects.filter(estado=estado)
        context = {
            'disponibles':disponibles
        }    
    except Estado.DoesNotExist:
        context = {}       
        
    return render(request, 'PaginaPrincipal/index.html', context)

def getdata(request):
    try:
        estado = Estado.objects.get(descripcion='Disponible')
        disponibles = Mascota.objects.filter(estado=estado)        
        jsondata = serializers.serialize('json', disponibles)
        return HttpResponse(jsondata)
    except Estado.DoesNotExist:
        return HttpResponse("Error")
    


def base_layout(request):
    template = 'PaginaPrincipal/base.html'
    return render(request, template)
