from django.db import models

# Create your models here.

#Modelo de datos

class Editorial(models.Model):
    nombre = models.CharField(unique=True,null=False)

    class Meta:
        db_table = 'Editorial'
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'