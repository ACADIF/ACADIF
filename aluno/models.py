"""Modelo base do ALUNO"""
from django.db import models

class Aluno(models.Model):
    """Dados do ALUNO"""
    alvos = (
        ("Ci","Concluiu"),
        ("Co","Cursando")
    )
    nome = models.CharField(max_length=30)
    matricula = models.IntegerField(primary_key=True)
    cpf = models.IntegerField(unique=True)
    born = models.DateField()
    endereco = models.CharField(max_length=120)
    estado = models.CharField(max_length=210, choices=alvos)
