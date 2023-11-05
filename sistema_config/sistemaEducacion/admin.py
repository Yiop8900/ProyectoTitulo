from django.contrib import admin
from .models import Comuna, Curso, Eventos, Rol, Usuario, Alumno, Apoderado, Profesor, Notas, Notificacion, Planificacion

# Registra tus modelos aquí para que se muestren en el panel de administración

admin.site.register(Comuna)
admin.site.register(Curso)
admin.site.register(Eventos)
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Alumno)
admin.site.register(Apoderado)
admin.site.register(Profesor)
admin.site.register(Notas)
admin.site.register(Notificacion)
admin.site.register(Planificacion)
