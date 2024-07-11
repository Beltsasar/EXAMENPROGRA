from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    def __str__(self):
        return f'{self.nombre}  {self.precio}'
    
    
    


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)
    nombre_completo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    comuna = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

from django.db import models

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.nombre} ({self.email})'
