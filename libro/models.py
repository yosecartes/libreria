from django.db import models

# Create your models here.

#Modelo de datos

class Libro(models.Model):
    nombre = models.CharField(unique=True,null=False)
    primera_edicio = models.IntegerField
    numero_paginas = models.IntegerField

    class Meta:
        db_table = 'Book'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = 'id'