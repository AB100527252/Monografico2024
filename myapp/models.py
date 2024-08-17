from django.db import models

# Create your models here.

class Partido(models.Model):
    nombre = models.CharField(max_length=100)
    ideologia = models.CharField(max_length=100)
    color = models.CharField(max_length=50)