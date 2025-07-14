from django.shortcuts import render, redirect
from .models import Recorrido
from .forms import PreinscripcionForm

def principal(request):
    recorridos = Recorrido.objects.all()
    return render(request, "recorridos/principal.html", {'recorridos': recorridos})

def detalle_recorrido(request):
    return render(request, "recorridos/detalle_recorrido.html")

def preinscripcion(request):
    if request.method == 'POST':
        form = PreinscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exitoso')  # Cambiado aquí
    else:
        form = PreinscripcionForm()
    return render(request, "recorridos/preinscripcion.html", {'form': form})

def exitoso(request):
    return render(request, "recorridos/exitoso.html") 
