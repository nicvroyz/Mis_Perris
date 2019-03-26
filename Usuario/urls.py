from django.urls import path, reverse_lazy
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from Mis_Perris import urls

app_name = 'Usuario'
urlpatterns = [
    # ex: /usuarios/
    path('', views.registrar_usuario, name='registrar_usuario'),
    #ex: /usuarios/5
    path('listar_usuarios/', views.listar_usuarios, name="listar_usuarios"),
    path('ajax/cargar_ciudades/', views.cargar_ciudades, name="cargar_ciudades"),    
    path('mi_cuenta/', views.mi_cuenta, name= 'mi_cuenta'),
]