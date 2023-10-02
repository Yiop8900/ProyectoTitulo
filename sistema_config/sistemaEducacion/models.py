from django.db import models

class Comuna(models.Model):
    id_comuna = models.PositiveSmallIntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=50)

class Curso(models.Model):
    id_curso = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=10)
    cant_alum = models.PositiveSmallIntegerField()

class Eventos(models.Model):
    id_evento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=4000)  # Reducir la longitud a 4000 o menos
    imagen = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return self.descripcion

class Rol(models.Model):
    id_rol = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

class Apoderado(models.Model):
    run = models.PositiveIntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    direccion = models.CharField(max_length=50)

class Profesor(models.Model):
    run = models.PositiveIntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()

class Notas(models.Model):
    id_notas = models.PositiveSmallIntegerField(primary_key=True)
    nota1 = models.FloatField(null=True)
    nota2 = models.FloatField(null=True)
    nota3 = models.FloatField(null=True)
    nota4 = models.FloatField(null=True)
    nota5 = models.FloatField(null=True)
    nota6 = models.FloatField(null=True)
    promedio = models.FloatField(null=True)

class Notificacion(models.Model):
    id_notificacion = models.PositiveSmallIntegerField(primary_key=True)
    fecha = models.DateField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=300)

class Planificacion(models.Model):
    id_plan = models.PositiveSmallIntegerField(primary_key=True)
    profesor_run = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    obj_clase = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    act_semestre = models.TextField(max_length=3000)

class Usuario(models.Model):
    id_usuario = models.PositiveSmallIntegerField(primary_key=True)
    correo = models.EmailField()
    contrasenia = models.CharField(max_length=20)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Alumno(models.Model):
    run = models.PositiveIntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    inf_adicional = models.TextField(max_length=300)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
