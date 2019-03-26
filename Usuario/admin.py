from django.contrib import admin
from .models import Usuario, Region, Ciudad, Tipo_Vivienda
from .forms import UsuarioForm

class UserAdmin(admin.ModelAdmin):
    form = UsuarioForm

# Register your models here.
admin.site.register(Usuario, UserAdmin)
admin.site.register(Region)
admin.site.register(Ciudad)


admin.site.register(Tipo_Vivienda)