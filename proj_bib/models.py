from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
class Usuario(models.Model):
    Nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=200,unique=True)
    data_criacao = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.Nome