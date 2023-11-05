from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .views import *
from django.db import connection
from django.http import JsonResponse
from django.contrib import messages
import json
from datetime import datetime
import base64
import hashlib
import matplotlib.pyplot as plt
import os
from django.conf import settings



# Create your views here.

from django.contrib.auth import login as auth_login




#ORIGINAL
def login(p_correo, p_contrasenia):
    django_cursor = connection.cursor()
    out_cur = django_cursor.connection.cursor()

    # Llama al procedimiento PL/SQL
    django_cursor.callproc("LOGIN", [p_correo, p_contrasenia, out_cur])

    # Recopila los resultados del cursor de referencia
    result = []
    for row in out_cur:
        result.append(row)

    return result

def index(request):
    is_login_successful = request.GET.get('is_login_successful', False)
    rol = iniciar_sesion(request)
    imagen = listar_evento()

    arreglo = []

    for i in imagen:
        data = {
            'data': i,
            'imagen': str(base64.b64encode(i[2].read()), 'utf-8')
        }
        arreglo.append(data)
    
    context = {
        'is_home': True,  # Establece esto en True para la página de inicio
        'is_login_successful': is_login_successful,
        'eventos' : arreglo,
        'rol': rol,
    
    }

    return render(request, 'index.html', context)


def base(request):
    is_login_successful = request.GET.get('is_login_successful', False)
    context = {  # Establece esto en True para la página de inicio
        'is_login_successful': is_login_successful,
    }
    return render(request, 'base.html', context)



def sistema_Profe(request):
    is_login_successful = request.GET.get('is_login_successful', False)
    context = {  # Establece esto en True para la página de inicio
        'is_login_successful': is_login_successful,
    
    }
    return render(request, 'Profesor/sistema_Profe.html',context)

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
    if request.method == 'POST':
        p_correo = request.POST.get('correo')
        p_contrasenia = request.POST.get('contrasenia')

        resultados = login(p_correo, p_contrasenia)

        if resultados:
            # Configuración específica de Swal para la alerta de éxito
            success_config = {
                'icon': 'success',
                'title': 'Inicio de sesión exitoso',
                'position': 'top-end',
            }

            return redirect(reverse('index') + '?is_login_successful=True' + json.dumps(success_config), resultados)


        else:
            # En caso de error, puedes manejar los mensajes de error como lo hacías antes
            messages.error(request, 'Correo o contraseña incorrectos')

    return render(request, 'iniciar_sesion.html')

def apoderado (request):

    return render (request, 'Apoderados_Alumnos/apoderado.html')

def revisar_notas (request):
    return render (request, 'Apoderados_Alumnos/revisar_notas.html')

def notificar (request):
    data = {
        'apoderados' : listar_apoderado()
    }

    return render (request, 'Profesor/notificar.html', data)

def dashboards(request):
    
    return render(request, 'Administrador/dashboard.html')

def admin_ap(request):
    if request.method == 'POST':
        p_run = request.POST.get("rut")
        p_dv = request.POST.get("dv")
        p_nombre = request.POST.get("nombre")
        p_apellido = request.POST.get("apellido")
        p_telefono = request.POST.get("telefono")
        p_direccion = request.POST.get("direccion")
        p_comuna_id = request.POST.get("comuna")
        p_rol_id = request.POST.get("rol")

        
        insert = insertar_apoderado(p_run, p_dv, p_nombre, p_apellido, p_telefono, p_direccion, p_comuna_id, p_rol_id)

        if insert:
            print("INSERCION EXITOSA!!")
        else:
            print("VUELVE A PROBAR")
        

    data = {
        'apoderados': listar_apoderado(),
        'apoderado_run': listar_apoderado_r(),
        'rol': listar_rol(),
        'comuna': listar_comunas(),
    }

    return render(request, 'Administrador/admin_apoderado.html', data)

def admin_al (request):
    if request.method == 'POST':
        p_run = request.POST.get("rut")
        p_dv = request.POST.get("dv")
        p_nombre = request.POST.get("nombre")
        p_apellido = request.POST.get("apellido")
        p_fecha_nac = request.POST.get("fecha")
        p_direccion = request.POST.get("direccion")
        p_telefono = request.POST.get("telefono")  
        p_inf_adicional = request.POST.get("inf_adicional")  
        p_comuna_id = request.POST.get("comuna")
        p_apoderado_id = request.POST.get("apoderado")
        p_notas_id = request.POST.get("nota")
        p_curso_id = request.POST.get("curso")
        p_rol_id = request.POST.get("rol")

        insert = insertar_alumno(p_run, p_dv, p_nombre, p_apellido, p_fecha_nac, p_direccion, p_telefono, p_inf_adicional, p_curso_id, p_comuna_id, p_apoderado_id, p_notas_id, p_rol_id)
        delete = eliminar_alumno(p_run)
        if insert:
            print("INSERCION EXITOSA!!")
        else:
            print("VUELVE A PROBAR")

    
    data = {
        'alumnos' : listar_alumnos(),
        'curso': listar_cursos(),
        'rol': listar_rol(),
        'comuna': listar_comunas(),
        'nota': listar_nota()
    }
    return render (request, 'Administrador/admin_alum.html', data)

def eliminar_alumno (p_run):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    cursor.callproc("DELETE_ALUMNO", [p_run])
       
    return True

def admin_pro (request):
    if request.method == 'POST':
        p_run = request.POST.get("rut")
        p_dv = request.POST.get("dv")
        p_nombre = request.POST.get("nombre")
        p_apellido = request.POST.get("apellido")
        p_direccion = request.POST.get("direccion")
        p_telefono = request.POST.get("telefono")    
        p_comuna_id = request.POST.get("comuna")
        p_curso_id = request.POST.get("curso")
        p_rol_id = request.POST.get("rol")

        
        insert = insertar_profesor(p_run, p_dv, p_nombre, p_apellido, p_direccion, p_telefono, p_comuna_id, p_curso_id, p_rol_id)

        if insert:
            print("INSERCION EXITOSA!!")
        else:
            print("VUELVE A PROBAR")

    data = {
        'profesores': listar_profesores(),
        'curso': listar_cursos(),
        'rol': listar_rol(),
        'comuna': listar_comunas(),
    }
    return render (request, 'Administrador/admin_profe.html',data)


def admin_user (request):
    if request.method == 'POST':
        p_correo = request.POST.get("correo")
        p_contrasenia = request.POST.get("contrasenia")
        p_rol_id = request.POST.get("rol")

        insert = insertar_admin(p_correo, p_contrasenia, p_rol_id)

        if insert:
            print("INSERCION EXITOSA!!")
        else:
            print("VUELVE A PROBAR")


    data = {
        'usuarios': listar_usuarios(),
        'rol': listar_rol()
    }
    return render(request, 'Administrador/admin_user.html', data)

def control_plan (request):
    return render (request, 'Administrador/control_plan.html')
##
def admin_evento (request):
    if request.method == "POST":
        p_descripcion = request.POST.get("descripcion")
        imagen_data = request.FILES.get("foto")
        p_profesor_id = request.POST.get("profe")

        # Lee los datos binarios del archivo y guárdalos en una variable
        p_imagen = imagen_data.read()

        # Luego, debes usar imagen_data para insertar la imagen en tu base de datos (esto depende de cómo esté definida tu función insertar_evento).
        
        # Por ejemplo, si tu función insertar_evento toma imagen_data como argumento, puedes llamarla de la siguiente manera:
        insert = insertar_evento(p_descripcion, p_imagen, p_profesor_id)

        if insert:
            print("INSERCIÓN EXITOSA!!")
        else:
            print("VUELVE A PROBAR")


    imagen = listar_evento()

    arreglo = []

    for i in imagen:
        data = {
            'data': i,
            'imagen': str(base64.b64encode(i[2].read()), 'utf-8')
        }
        arreglo.append(data)

    data = {
        'usuarios': listar_usuarios(),
        'rol': listar_rol(),
        'eventos': arreglo,
        'profesor': listar_profesores_esp()
    }
    return render (request, 'Administrador/admin_evento.html', data)
###

def admin_grafico (request):
    
    return render (request, 'Administrador/dashboard.html')

def pagoMatricula(request):
    return render(request, 'Apoderados_Alumnos/pagoMatricula.html')

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

def listar_apoderado_r():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_APODERADO_R", [out_cur])

    lista_apo_r = []

    for fila in out_cur:
        lista_apo_r.append(fila)
        

    return lista_apo_r

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

def listar_profesores_esp():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_PROFESOR_ESP", [out_cur])

    lista_prof = []

    for fila in out_cur:
        lista_prof.append(fila)

    return lista_prof


def listar_comunas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_COMUNA", [out_cur])

    lista_com = []
    
    for fila in out_cur:
        lista_com.append(fila)
    return lista_com

def listar_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_USUARIO", [out_cur])

    lista_user = []

    for fila in out_cur:
        lista_user.append(fila)

    return lista_user

def listar_cursos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_CURSO", [out_cur])

    lista_curso = []

    for fila in out_cur:
        lista_curso.append(fila)

    return lista_curso


def cbo_usuario():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("CBO_USUARIO", [out_cur])

    lista_cr = []

    for fila in out_cur:
        lista_cr.append(fila)

    return lista_cr

def listar_rol():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_ROL", [out_cur])

    lista_rol = []

    for fila in out_cur:
        lista_rol.append(fila)

    return lista_rol

def listar_nota():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_NOTAS", [out_cur])

    lista_nota = []

    for fila in out_cur:
        lista_nota.append(fila)
    return lista_nota

def listar_evento():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_EVENTOS", [out_cur])

    lista_e = []

    for fila in out_cur:
        lista_e.append(fila)
    return lista_e

def insertar_apoderado(p_run, p_dv, p_nombre, p_apellido, p_telefono, p_direccion, p_comuna_id, p_rol_id):
    # Establecer una conexión a la base de datos
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    try:
        # Llamar a la función almacenada "INSERT_APODERADO" con los parámetros
        cursor.callproc("INSERT_APODERADO", (p_run, p_dv, p_nombre, p_apellido, p_telefono, p_direccion, p_comuna_id, p_rol_id))
        
        # Confirmar los cambios en la base de datos
        django_cursor.connection.commit()
        
        # Devolver True para indicar que la inserción se realizó correctamente
        return True
    except Exception as e:
        # En caso de error, puedes manejar la excepción aquí, por ejemplo, registrando el error
        # y devolviendo False para indicar que la inserción falló
        print(f"Error al insertar apoderado: {e}")
        return False
    finally:
        # Asegúrate de cerrar el cursor y liberar los recursos
        cursor.close()

def insertar_profesor(p_run, p_dv, p_nombre, p_apellido, p_direccion, p_telefono, p_comuna_id, p_curso_id, p_rol_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    try:
        # Llamar a la función almacenada "INSERT_APODERADO" con los parámetros
        cursor.callproc("INSERT_PROFESOR", (p_run, p_dv, p_nombre, p_apellido, p_direccion, p_telefono, p_comuna_id, p_curso_id, p_rol_id))

        cursor.connection.commit()
        
        print("correcto")

    except Exception as e:
        # En caso de error, puedes manejar la excepción aquí, por ejemplo, registrando el error
        # y devolviendo False para indicar que la inserción falló
        print(f"Error al insertar apoderado: {e}")
        return False
    finally:
        # Asegúrate de cerrar el cursor y liberar los recursos
        cursor.close()

def insertar_alumno(p_run, p_dv, p_nombre, p_apellido, p_fecha_nac, p_direccion, p_telefono, p_inf_adicional, p_curso_id, p_comuna_id, p_apoderado_id, p_notas_id, p_rol_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    try:

        cursor.callproc("INSERT_ALUMNO", (p_run, p_dv, p_nombre, p_apellido, p_fecha_nac, p_direccion, p_telefono, p_inf_adicional, p_curso_id, p_comuna_id, p_apoderado_id, p_notas_id, p_rol_id))
        cursor.connection.commit()
        
        print("correcto")

    except Exception as e:
        # En caso de error, puedes manejar la excepción aquí, por ejemplo, registrando el error
        # y devolviendo False para indicar que la inserción falló
        print(f"Error al insertar alumno: {e}")
        return False
    finally:
        # Asegúrate de cerrar el cursor y liberar los recursos
        cursor.close()

def insertar_admin(p_correo, p_contrasenia, p_rol_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    try:

        cursor.callproc("INSERT_USUARIO", (p_correo, p_contrasenia, p_rol_id))
        cursor.connection.commit()
        
        print("correcto")

    except Exception as e:

        print(f"Error al insertar administrador: {e}")
        return False
    finally:
        # Asegúrate de cerrar el cursor y liberar los recursos
        cursor.close()

def insertar_notificacion(p_fecha, p_asunto, p_mensaje):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    try:

        cursor.callproc("INSERT_NOTIFICAR", (p_fecha, p_asunto, p_mensaje))
        cursor.connection.commit()
        
        print("correcto")

    except Exception as e:

        print(f"Error al insertar notificacion: {e}")
        return False
    finally:
        # Asegúrate de cerrar el cursor y liberar los recursos
        cursor.close()

def insertar_evento(p_descripcion, p_imagen, p_profesor_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    try:
        # Llamar a la función almacenada "INSERT_EVENTOS" con los parámetros
        cursor.callproc("INSERT_EVENTOS", (p_descripcion, p_imagen, p_profesor_id))

        cursor.connection.commit()
        
        print("correcto")
        

    except Exception as e:
        # En caso de error, puedes manejar la excepción aquí, por ejemplo, registrando el error
        # y devolviendo False para indicar que la inserción falló
        print(f"Error al insertar Evento: {e}")
        return False
    finally:
        # Asegúrate de cerrar el cursor y liberar los recursos
        cursor.close()
        
def eliminar_evento(p_evento_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    try:
        # Llamar al procedimiento almacenado "DELETE_EVENTO" con el parámetro
        cursor.callproc("DELETE_EVENTOS", (p_evento_id))
        cursor.connection.commit()
        print("Evento eliminado correctamente")

    except Exception as e:
        # En caso de error, puedes manejar la excepción aquí, por ejemplo, registrando el error
        # y devolviendo False para indicar que la eliminación falló
        print(f"Error al eliminar Evento: {e}")
        return False
    finally:
        # Asegúrate de cerrar el cursor y liberar los recursos
        cursor.close()



        
def eliminar_apoderado(p_run):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    try:

        cursor.callproc("DELETE_APODERADO", (p_run))
        cursor.connection.commit()
        
        print("eliminado")

    except Exception as e:

        print(f"Error al insertar notificacion: {e}")
        return False
    finally:
        # Asegúrate de cerrar el cursor y liberar los recursos
        cursor.close()




def listar_eventos_finales():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("LIST_EVENTOS", [out_cur])

    lista_e = []

    for fila in out_cur:
        lista_e.append(fila)
    return lista_e


def borrar_apoderado(request, p_run):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    cursor.callproc('DELETE_APODERADO', (p_run,))
    cursor.connection.commit()

    # Redireccionar a una página diferente después de eliminar el apoderado
    return HttpResponseRedirect('/admin_apoderado/')  # Reemplaza '/pagina_de_exito/' con la URL que desees redirigir

def borrar_profesor(request, p_run):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()

    cursor.callproc('DELETE_PROFESOR', (p_run,))
    cursor.connection.commit()

    # Redireccionar a una página diferente después de eliminar el apoderado
    return HttpResponseRedirect('/admin_profesor/')  # Reemplaza '/pagina_de_exito/' con la URL que desees redirigir



    



        