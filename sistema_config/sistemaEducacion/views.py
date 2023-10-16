from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .views import *
from django.db import connection
import cx_Oracle

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

def admin_ap(request):
    data = {
        'apoderados' : listar_apoderado()
    }

    return render(request, 'Administrador/admin_apoderado.html', data)

def admin_al (request):
    data = {
        'alumnos' : listar_alumnos()
    }
    return render (request, 'Administrador/admin_alum.html', data)

def admin_pro (request):
    return render (request, 'Administrador/admin_profe.html')

def admin_user (request):
    return render(request, 'Administrador/admin_user.html')

def control_plan (request):
    return render (request, 'Administrador/control_plan.html')



#-------- cosas ---------------

def listar_apoderado():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_APODERADO", [out_cur])

    lista_apo = []

    for fila in out_cur:
        lista_apo.append(fila)

    return lista_apo

def listar_alumnos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_ALUMNO", [out_cur])

    lista_al = []

    for fila in out_cur:
        lista_al.append(fila)

    return lista_al

def listar_apoderado():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_APODERADO", [out_cur])

    lista_apo = []

    for fila in out_cur:
        lista_apo.append(fila)

    return lista_apo