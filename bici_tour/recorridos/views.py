from django.shortcuts import render, redirect
from .models import Recorrido
from .forms import PreinscripcionForm

def principal(request):
    recorridos = Recorrido.objects.all()
    return render(request, "recorridos/principal.html", {'recorridos': recorridos})
