from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    mail_usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    fecha_registro = models.DateField()

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=50)

class Foro(models.Model):
    id_foro = models.AutoField(primary_key=True)
    nombre_foro = models.CharField(max_length=100)
    descripcion_foro = models.CharField(max_length=500)

class Tema(models.Model):
    id_tema = models.AutoField(primary_key=True)
    id_foro = models.ForeignKey(Foro, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo_tema = models.CharField(max_length=200)
    primer_mensaje = models.CharField(max_length=4000)
    fecha_creacion = models.DateField()

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    id_tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido_post = models.CharField(max_length=4000)
    fecha_publicacion = models.DateField()

class Moderador(models.Model):
    id_moderador = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_foro = models.ForeignKey(Foro, on_delete=models.CASCADE)
