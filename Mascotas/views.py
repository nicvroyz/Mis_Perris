from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Mascota, Estado
from Usuario.models import Usuario
from .forms import MascotaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    estado = Estado.objects.get(descripcion='Disponible')
    disponibles = Mascota.objects.filter(estado=estado)
    context = {
        'disponibles':disponibles
    }
    return render(request, 'Mascotas/index.html', context)

@login_required
def registrar_mascota(request):
    estados = Estado.objects.all()
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print('Todo bien')
            form.save()            
            message = '%s agregada de forma exitosa'%form.cleaned_data['nombre']
            mascotas = Mascota.objects.all()
            estados = Estado.objects.all()
            context = {
                'mascotas': mascotas,
                'estados': estados,
                'message':message
            }
            return render(request, 'Mascotas/lista_perritos.html', context)
        else:
            return render(request, 'Mascotas/registrar_mascotas.html', {'estados': estados})        
    return render(request, 'Mascotas/registrar_mascotas.html', {'estados': estados})

@login_required
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    estados = Estado.objects.all()
    context = {
        'mascotas': mascotas,
        'estados': estados
    }
    return render(request, 'Mascotas/lista_perritos.html', context)
@login_required
def editar_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)    
    estados = Estado.objects.all()
    context = {
        'mascota': mascota,
        'estados': estados
    }
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)        
        if form.is_valid():            
            mascota_form = MascotaForm(request.POST, request.FILES, instance=mascota)
            mascota_form.save(commit=True)
            print("Hola")
            message = '%s editada de forma exitosa'%form.cleaned_data['nombre']
            mascotas = Mascota.objects.all()
            estados = Estado.objects.all()
            context = {
                'mascotas': mascotas,
                'estados': estados,
                'message':message
            }
            return render(request, 'Mascotas/lista_perritos.html', context)
        else:
            return render(request, 'Mascotas/editar_mascota.html', context)
    else:    
        return render(request, 'Mascotas/editar_mascota.html', context)
@login_required
def borrar_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.fotografia.delete()
        message = '%s borrada de forma exitosa'%mascota.nombre
        mascota.delete()
        
        mascotas = Mascota.objects.all()
        estados = Estado.objects.all()
        context = {
            'mascotas': mascotas,
            'estados': estados,
            'message':message
        }
        return render(request, 'Mascotas/lista_perritos.html', context)
    return render(request, 'Mascotas/borrar_mascota.html', {'mascota':mascota})

def seleccionar_mascota_estado(request):    
    if request.GET.get('estado_id') == str(-1):
        print('llega hasta aca!!!')
        mascotas = Mascota.objects.all()
        estados = Estado.objects.all()
        context = {
            'mascotas': mascotas,
            'estados': estados
        }
        return render(request, 'Mascotas/listar_mascotas_estado.html', context)
    else:
        estado = request.GET.get('estado_id')
        mascotas = Mascota.objects.filter(estado = estado)
        estados = Estado.objects.all()
        context = {
            'mascotas': mascotas,
            'estados': estados
        }
        return render(request, 'Mascotas/listar_mascotas_estado.html', context)

@login_required
def adoptar(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    estado = Estado.objects.get(descripcion='Adoptado')
    usuario = Usuario.objects.get(rut=request.user)
    mascota.estado = estado
    mascota.usuario = usuario
    mascota.save()       
    return HttpResponseRedirect('/')

