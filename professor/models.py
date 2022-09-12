from django.db import models


class Professor(models.Model):
    """Dados do PROFESSOR"""
    NOME = models.CharField(max_length=30)
    CPF = models.IntegerField(unique=True)
    BORN = models.DateField(verbose_name=str)
    ENDERECO = models.CharField(max_length=50)
    SALARIO = models.FloatField()
    """titulação a decidir"""


class insituicao(models.Model):
    """instituição de formação do PROFESSOR"""
    NOME = models.CharField(max_length=100)

class grau(models.Model):
    alvos = (
        ("B","Bacharelado"),
        ("L","Licenciatura"),
        ("T","Tecnólogo")
    )

    grau = models.CharField(max_length=15, choices=alvos)