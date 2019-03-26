from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='Mascotas'

urlpatterns=[
    # ex: Mascotas
    path('', views.index, name="index"),
    path('registrar/', views.registrar_mascota, name="registrar_mascota"),
    path('listar_mascotas/',  views.listar_mascotas, name="listar_mascotas"),
    path('editar_mascota/<int:id_mascota>', views.editar_mascota, name="editar_mascota"),
    path('borrar_mascota/<int:id_mascota>', views.borrar_mascota, name="borrar_mascota"),
    path('ajax/seleccionar_mascota_estado', views.seleccionar_mascota_estado, name="seleccionar_mascota_estado"),
    path('adoptar/<int:id_mascota>', views.adoptar, name="adoptar")
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)