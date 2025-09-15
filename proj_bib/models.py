from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
class Usuario(models.Model):
    Nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=200,unique=True)
    data_criacao = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.Nome,self.data_criacao

class emprestimo(models.Model):
    user=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprest=models.DeteField()
    data_devol=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=20,choices=[('Aberto,','Aberto'),('Devolvido','Devolvido')])

    def __str__(self):
        return  f"{self.user}->{self.livro}"