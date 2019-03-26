from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='Pagina_Principal'

urlpatterns=[
    # ex: Mascotas
    path('', views.index, name="index"),
    path('base_layout',views.base_layout,name='base_layout'),   
    path('getdata',views.getdata,name='getdata')
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)