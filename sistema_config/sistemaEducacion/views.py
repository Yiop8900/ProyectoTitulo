from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .views import *
from django.db import connection

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
    data = {
        'alumnos': listar_alumnos()
    }
    return render(request, 'Profesor/clase.html', data)

def planificar(request):

    return render(request, 'Profesor/planificar.html')

def calificar(request):
    return render(request, 'Profesor/calificar.html')

def iniciar_sesion(request):
    mensaje = ""  # Inicializa el mensaje como nulo

    if request.method == 'POST':
        p_correo = request.POST.get('correo')
        p_contrasenia = request.POST.get('contrasenia')

        resultados = login(p_correo, p_contrasenia)

        if resultados:
            # Suponiendo que `resultados` es una lista de resultados de la función `login`
            return render(request, 'index.html')
            # Puedes realizar otras acciones aquí, como establecer una sesión de usuario, redirigir, etc.
        else:
            mensaje = 'CORREO O CONTRASENIA INCORRECTOS'

    return render(request, 'iniciar_sesion.html', {'mensaje': mensaje})



def apoderado (request):

    return render (request, 'Apoderados_Alumnos/apoderado.html')

def revisar_notas (request):
    return render (request, 'Apoderados_Alumnos/revisar_notas.html')

def notificar (request):
    data = {
        'apoderados' : listar_apoderado()
    }

    return render (request, 'Profesor/notificar.html', data)

def admin_ap(request):
    data = {
        'apoderados' : listar_apoderado(),
        'correo': cbo_usuario(),
    }

    return render(request, 'Administrador/admin_apoderado.html', data)

def admin_al (request):
    data = {
        'alumnos' : listar_alumnos()
    }
    return render (request, 'Administrador/admin_alum.html', data)

def admin_pro (request):
    data = {
        'profesores': listar_profesores()
    }
    return render (request, 'Administrador/admin_profe.html',data)

def admin_user (request):
    data = {
        'usuarios': listar_usuarios()
    }
    return render(request, 'Administrador/admin_user.html', data)

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

def listar_profesores():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_PROFESOR", [out_cur])

    lista_pro = []

    for fila in out_cur:
        lista_pro.append(fila)

    return lista_pro


def listar_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_USUARIO", [out_cur])

    lista_user = []

    for fila in out_cur:
        lista_user.append(fila)

    return lista_user

def login(p_correo, p_contrasenia):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LOGIN", [p_correo, p_contrasenia, out_cur])

    list_log = []

    for fila in out_cur:
        list_log.append(fila)

    return list_log

def cbo_usuario():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("CBO_USUARIO", [out_cur])

    lista_cr = []

    for fila in out_cur:
        lista_cr.append(fila)

    return lista_cr