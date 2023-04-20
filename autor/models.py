from django.db import models

# Create your models here.

#Modelo de datos

class Autor(models.Model):
    nombre = models.CharField(unique=True,null=False)

    class Meta:
        db_table = 'Authors'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'