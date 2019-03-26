from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Usuario, Tipo_Vivienda, Region, Ciudad


class UsuarioForm(forms.ModelForm):  
    correo_electronico = forms.EmailField(error_messages={'required': 'El correo electrónico es obligatorio'})   
    rut = forms.SlugField(error_messages={'required': 'El rut es obligatorio'})    
    password = forms.CharField(error_messages={'required': 'El password es obligatorio'})
    password_verification = forms.CharField(error_messages={'required': 'La verificación de password es obligatoria'})
    nombre_completo = forms.CharField(error_messages={'required': 'El nombre completo es obligatorio'})
    fecha_nacimiento = forms.DateField(error_messages={'required': 'La fecha de nacimiento es obligatoria'})
    telefono = forms.IntegerField(error_messages={'required': 'El teléfono es obligatorio'})
    region = forms.ModelChoiceField(queryset=Region.objects.all(), error_messages={'required': 'La región es obligatoria'})
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), error_messages={'required': 'La ciudad es obligatoria'})
    tipo_vivienda = forms.ModelChoiceField(queryset=Tipo_Vivienda.objects.all(), error_messages={'required': 'El tipo de vivienda es obligatorio'})
    class Meta:
        model = Usuario
        widgets = {
            'password': forms.PasswordInput(attrs={'readonly': 'readonly'}),
            'password_verification': forms.PasswordInput(attrs={'readonly': 'readonly'})
        }
        fields = '__all__'
                       

class UsuarioLoginForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('rut', 'password')
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }
        labels = {
            'rut': _('RUT'),
            'password': _('Contraseña')
        }
      