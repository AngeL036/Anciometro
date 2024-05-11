from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ansiedad(models.Model):
    id = models.AutoField(primary_key=True)
    respuestas = models.CharField(max_length=12)
    fecha = models.DateTimeField()
    nombreUser = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(blank=True,null=True)

class depresion(models.Model):
    id = models.AutoField(primary_key=True)
    respuestas = models.CharField(max_length=12) 
    fecha = models.DateTimeField()
    nombreUser = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(blank=True,null=True)
