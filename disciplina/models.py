"""Disciplinas do curso"""
from django.db import models



class disciplina(models.Model):
    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=300)
    

    def __str__(self) -> str:
        return f"Diciplina de {self.nome}"