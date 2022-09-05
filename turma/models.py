from django.db import models
from aluno.models import Aluno
from disciplina.models import disciplina
from django.contrib.auth import get_user_model


class turma_semestre(models.Model):
    cadeiras = models.ForeignKey(disciplina, on_delete=models.SET_DEFAULT, default=None)
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(get_user_model(), related_name="aluno da turma"),