from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    primerNombre = models.CharField(max_length=128)
    segundoNombre = models.CharField(max_length=128, null=True)
    apellidoPaterno = models.CharField(max_length=128)
    apellidoMaterno = models.CharField(max_length=128)
    fechaNacimiento = models.DateField()
