from django.shortcuts import render
from .views import *
import requests

# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    context = {
        'is_home': True  # Establece esto en True para la página de inicio
    }
    return render(request, 'index.html', context)

def sistema_Profe(reuqest):
    return render(reuqest, 'Profesor/sistema_Profe.html')

def clase(reuqest):
    return render(reuqest, 'Profesor/clase.html')

def planificar(reuqest):
    return render(reuqest, 'Profesor/planificar.html')

def calificar(reuqest):
    return render(reuqest, 'Profesor/calificar.html')

def iniciar_sesion(reuqest):
    return render(reuqest, 'iniciar_sesion.html')