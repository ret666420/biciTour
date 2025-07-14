from django import forms
from .models import Preinscripcion

class PreinscripcionForm(forms.ModelForm):
    class Meta:
        model = Preinscripcion
        fields = ['nombre', 'correo', 'telefono', 'ciudad', 'estado', 'recorrido']
        