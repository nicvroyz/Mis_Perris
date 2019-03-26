from django import forms
from .models import Mascota, Estado

class MascotaForm(forms.ModelForm):
    nombre = forms.CharField(error_messages={'required': 'El nombre de la mascota es obligatorio.'})
    fotografia = forms.ImageField(error_messages={'required': 'La fotografía de la mascota es obligatoria.'})
    raza = forms.CharField(error_messages={'required': 'La raza de la mascota es obligatoria.'})
    descripcion = forms.CharField(error_messages={'required': 'La descripción de la mascota es obligatoria.'})
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), error_messages={'required': 'El estado de la mascota es obligatorio.'})
    class Meta:
        model = Mascota
        fields = '__all__'
        exclude = ('usuario',)