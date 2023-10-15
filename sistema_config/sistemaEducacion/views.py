from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .views import *
import requests
from django.db import connections


# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    context = {
        'is_home': True  # Establece esto en True para la página de inicio
    }
    return render(request, 'index.html', context)

def sistema_Profe(request):
    return render(request, 'Profesor/sistema_Profe.html')

def clase(request):
    return render(request, 'Profesor/clase.html')

def planificar(request):
    return render(request, 'Profesor/planificar.html')

def calificar(request):
    return render(request, 'Profesor/calificar.html')

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html')

def apoderado (request):
    return render (request, 'Apoderados_Alumnos/apoderado.html')

def revisar_notas (request):
    return render (request, 'Apoderados_Alumnos/revisar_notas.html')

def notificar (request):
    return render (request, 'Profesor/notificar.html')

def admin_ap (request):


    



    return render (request, 'Administrador/admin_apoderado.html')

def admin_al (request):
    return render (request, 'Administrador/admin_alum.html')

def admin_pro (request):
    return render (request, 'Administrador/admin_profe.html')

def admin_user (request):
    return render (request, 'Administrador/admin_user.html')

def control_plan (request):
    return render (request, 'Administrador/control_plan.html')