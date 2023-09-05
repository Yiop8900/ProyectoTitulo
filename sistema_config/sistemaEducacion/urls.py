from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('base/', base, name='base'),
    path('sistema_Profe/', sistema_Profe, name='sistema_Profe'),
    path('calificar/', calificar, name='calificar'),    
    path('planificar/', planificar, name='planificar'),
    path('clase/', clase, name='clase'), 
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('apoderado/', apoderado , name= 'apoderado'),
]