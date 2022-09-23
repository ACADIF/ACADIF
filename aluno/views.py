"""Views do ALUNO"""
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods

from aluno.models import Aluno

@require_http_methods(["GET"])
def get_Alunos(request):
    """Retorna os dados de todos os aluno"""
    aluno = Aluno.objects.all()
    resp_json = serializers.serialize("json", aluno)
    return HttpResponse (resp_json, content_type="application/json")

@require_http_methods(["POST"])
def post_Aluno(request):
    """Adiciona um ALUNO."""
    nova = Aluno()
    nova.user = get_user_model().objects.get(pk=request.POST["user_id"])
    nova.sexo = request.POST["sexo"]
    nova.rg = request.POST["rg"]
    nova.telefone = request.POST["telefone"]
    nova.matricula = request.POST["matricula"]
    nova.cpf = request.POST["cpf"]
    nova.born = request.POST["born"]
    nova.endereco = request.POST["endereco"]
    nova.estado_civil = request.POST["estado_civil"]
    nova.telefone = request.POST["telefone"]
    nova.nome_pai = request.POST["nome_pai"]
    nova.save()
    return HttpResponse("Aluno salvo com sucedida")

@require_http_methods(["DELETE"])
def delete_Aluno(request, Aluno_matricula):
    post = Aluno.objects.get(pk=Aluno_matricula)
    post.delete()

    return HttpResponse("Deletado com sucesso.")
