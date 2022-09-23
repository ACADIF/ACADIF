"""Modelo base do ALUNO"""
from enum import unique
from django.db import models
from django.contrib.auth import get_user_model
class Aluno(models.Model):
    """Dados do ALUNO"""
<<<<<<< Updated upstream
    nome = models.CharField(max_length=30)
    mat = models.IntegerField(primary_key=True)
=======
    choice = (
        ("C","casado"),
        ("S","solteiro"),
    )
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        null=False,
        related_name="Aluno",
        )
    matricula = models.IntegerField(unique=True)
    endereco = models.CharField(max_length=120)
    born = models.DateField()
    cpf = models.IntegerField()
    nome_pai = models.CharField(max_length=120)
    nome_mae = models.CharField(max_length=120)
    sexo = models.CharField(max_length=1)
    telefone = models.CharField(max_length=15)
    estado_civil = models.CharField(max_length=120, choices=choice)
    rg = models.CharField(max_length=10)
>>>>>>> Stashed changes
