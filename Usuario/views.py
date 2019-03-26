from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .forms import UsuarioForm, UsuarioLoginForm
from .models import Usuario, Tipo_Vivienda, Region, Ciudad
from Mascotas.models import Mascota


# Create your views here.
def registrar_usuario(request):
    # Pantalla registro usuario.

    # Recuperar todos los tipos de vivienda.
    tipo_vivienda = Tipo_Vivienda.objects.all()
    # Recuperar las regiones.
    region = Region.objects.all()
    # Recuperar las ciudades, luego se cargan en base a selección
    # de Región.
    ciudad = Ciudad.objects.all()
    # Creación context, valores que se pasarán al template en caso
    # de no ser un request.POST
    context = {
        'tipos_viviendas': tipo_vivienda,
        'regiones': region,
        'ciudades': ciudad,        
    }
    if request.method == "POST":
        form = UsuarioForm(request.POST)       
        if form.is_valid():
            # Se limpia la información recuperada desde el formulario.            
            username = form.cleaned_data['rut']
            email = form.cleaned_data['correo_electronico']
            passwd = form.cleaned_data['password']
            # Se crea una instancia nueva del tipo User.
            # Esta permitirá login y manejo de cuentas. 
            user = User.objects.create_user(username, email, passwd)
            user.save()
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form)
            context = {
                'tipos_viviendas': tipo_vivienda,
                'regiones': region,
                'ciudades': ciudad,
                'form': form
            }
            # Si el formulario no es válido se redirecciona al mismo
            # form (registrar_usuario)
            return render(request, 'Usuario/registrar_usuario.html', context)
    else:
        return render(request, 'Usuario/registrar_usuario.html', context)
    
@login_required
def listar_usuarios(request):
    # Pantalla lista usuarios    

    # Se recuperan todos los usuarios de las base de datos.
    usuarios = Usuario.objects.all()
    # Creación context, valores que se pasarán al template.
    context = { 'usuarios': usuarios }
    return render(request, 'Usuario/listar_usuarios.html', context)

@login_required
def mi_cuenta(request):
    usuarios = Usuario.objects.get(rut=request.user)
    mascota = Mascota.objects.filter(usuario=usuarios)
    context = {
        'usuarios' : usuarios,
        'mascota' : mascota
    }
    return render(request, 'Usuario/mi_cuenta.html', context)


def cargar_ciudades(request):
    # Carga de ciudades según región seleccionada.
    region_id = request.GET.get('region_id')
    ciudades = Ciudad.objects.filter(numero_region=region_id)
    return render(request, 'Usuario/cargar_ciudades.html', {'ciudades': ciudades})

