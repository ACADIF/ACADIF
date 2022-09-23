from msilib.schema import Binary
from secrets import choice
from django.db import models
from django.contrib.auth import get_user_model

class Egresso(models.Model):
    choice = (
        ("C","casado"),
        ("S","solteiro"),
    )
    """models do engressos"""
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        null=False
        )
    nome = models.CharField(max_length = 40)
    matricula = models.IntegerField(unique=True)
    endereco = models.CharField(max_length=120)
    born = models.DateField()
    cpf = models.IntegerField()
    nome_pai = models.CharField(max_length=120)
    nome_mae = models.CharField(max_length=120)
    sexo = models.CharField(max_length=1)
    telefone = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=120, choices=choice)
    