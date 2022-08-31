<<<<<<< Updated upstream
"""ORM do usuario"""
from django.db import models
from django.utils import timezone

# Create your models here.
class Aluno(models.Model):
    """criando os dados do usuario(aluno)"""

    name = models.CharField(max_length=140)
    matricula = models.DateTimeField(max_length=140,primary_key=True)
=======
"""Modelo base do ALUNO"""
from django.db import models

class Aluno(models.Model):
    """Dados do ALUNO"""

    nome = models.CharField(max_length=30)
    mat = models.IntegerField(primary_key=True)
>>>>>>> Stashed changes
