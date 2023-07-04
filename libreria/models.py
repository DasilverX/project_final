from django.db import models

# Create your models here.
class pacientes(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')