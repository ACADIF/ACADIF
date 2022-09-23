"""Modelo base do ALUNO"""
from enum import unique
from django.db import models
from django.contrib.auth import get_user_model
from aluno.models import Aluno
class Pais_aluno(models.Model):
    """Dados do pai do aluno"""
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE,
        null=False,
        related_name="pai de aluno +",
        )
    filho = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING, related_name="filho")
    endereco = models.CharField(max_length=120)
    born = models.DateField()
    cpf = models.IntegerField()
    telefone = models.CharField(max_length=15)
    rg = models.CharField(max_length=9)