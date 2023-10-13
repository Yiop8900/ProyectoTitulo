from django.db import models

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nom_comuna = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_comuna


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=20)
    tipo_usuario = models.IntegerField()
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    alumno_run = models.IntegerField(null=True)
    profesor_run = models.IntegerField(null=True)
    apoderado_run = models.IntegerField(null=True)

class Apoderado(models.Model):
    run = models.AutoField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    cant_alum = models.IntegerField()

class Notas(models.Model):
    id_notas = models.AutoField(primary_key=True)
    nota1 = models.FloatField(null=True)
    nota2 = models.FloatField(null=True)
    nota3 = models.FloatField(null=True)
    nota4 = models.FloatField(null=True)
    nota5 = models.FloatField(null=True)
    nota6 = models.FloatField(null=True)
    promedio = models.FloatField(null=True)

class Alumno(models.Model):
    run = models.AutoField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=30)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    inf_adicional = models.TextField(max_length=300)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
    notas = models.ForeignKey(Notas, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Profesor(models.Model):
    run = models.AutoField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Eventos(models.Model):
    id_evento = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=500)
    imagen = models.BinaryField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=300)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

class Planificacion(models.Model):
    id_plan = models.AutoField(primary_key=True)
    obj_clase = models.TextField(max_length=100)
    status = models.CharField(max_length=1)
    act_semestre = models.TextField(max_length=3000)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
