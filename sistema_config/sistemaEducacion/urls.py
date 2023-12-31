from django.urls import path
from .views import *
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'),
    path('sistema_Profe/', sistema_Profe, name='sistema_Profe'),
    path('calificar/', calificar, name='calificar'),    
    path('planificar/', planificar, name='planificar'),
    path('clase/', clase, name='clase'), 
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('apoderado/', apoderado , name= 'apoderado'),
    path('revisar_notas/', revisar_notas , name= 'revisar_notas'),
    path('notificar/', notificar , name= 'notificar'),
    path('admin_apoderado/', admin_ap , name= 'admin_apoderado'),
    path('admin_alum/', admin_al , name= 'admin_alum'),
    path('admin_profe/', admin_pro , name= 'admin_profe'),
    path('admin_user/', admin_user , name= 'admin_user'),
    path('control_plan/', control_plan , name= 'control_plan'),
    path('admin_evento/', admin_evento , name= 'admin_evento'),
    path('dashboards/', dashboards , name= 'dashboards'),
    path('pagoMatricula/', pagoMatricula , name= 'pagoMatricula'),
    path('borrar_apoderado/<str:p_run>/', borrar_apoderado , name= 'borrar_apoderado'),
    path('borrar_profesor/<str:p_run>/', borrar_profesor , name= 'borrar_profesor'),
    path('borrar_alumno/<str:p_run>/', borrar_alumno , name= 'borrar_alumno'),
    path('borrar_usuario/<str:p_id>/', borrar_usuario , name= 'borrar_usuario'),
    path('admin_apoderadoModi/<str:p_run>/', admin_apoderadoModi, name='admin_apoderadoModi'),
    path('admin_profeModi/<p_run>/', admin_profeModi, name='admin_profeModi'),
    path('admin_alumModi/<p_run>/', admin_alumModi, name='admin_alumModi'),


    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)