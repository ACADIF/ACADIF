"""Modelo base do ALUNO"""
from django.db import models

class Aluno(models.Model):
    """Dados do ALUNO"""
    nome = models.CharField(max_length=30)
    mat = models.IntegerField(primary_key=True)
