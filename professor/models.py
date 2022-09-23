from django.db import models

from django.contrib.auth import get_user_model
class Titulo(models.Model):
    """titulos de formação do PROFESSOR"""
    alvos = (
        ("B","Bacharelado"),
        ("L","Licenciatura"),
        ("T","Tecnólogo")
    )
    formacao = models.CharField(max_length=100)
    grau = models.CharField(max_length=15, choices=alvos)
    instituicao = models.CharField(max_length=120)

class Professor(models.Model):
    """Dados do PROFESSOR"""
    user = models.OneToOneField(
        get_user_model(),
        primary_key=True,
        on_delete=models.CASCADE
        )
    CPF = models.IntegerField(unique=True)
    BORN = models.DateField()
    ENDERECO = models.CharField(max_length=50)
    SALARIO = models.FloatField()
    TITULO = models.ForeignKey(Titulo, on_delete=models.CASCADE, default=None)


