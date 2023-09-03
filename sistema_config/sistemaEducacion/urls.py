from django.urls import path
from .views import *


urlpatterns = [
    path('', base, name='base'),
    path('index/', index, name='index'),
    path('sistema_Profe/', sistema_Profe, name='sistema_Profe'),
    path('calificar/', calificar, name='calificar'),    
    path('planificar/', planificar, name='planificar'),
    path('clase/', clase, name='clase'), 
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),  

]