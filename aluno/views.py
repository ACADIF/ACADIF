"""Views do ALUNO"""
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core import serializers

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
    nova.nome = request.POST["nome"]
    nova.mat = request.POST["mat"]
    nova.save()
    return HttpResponse("Aluno salvo com sucedida")

@require_http_methods(["DELETE"])
def delete_Aluno(request, Aluno_matricula):
    post = Aluno.objects.get(pk=Aluno_matricula)
    post.delete()

    return HttpResponse("Deletado com sucesso.")

@require_http_methods(["GET"])
def get_aluno(request, aluno_id):
    """Retorna aluno especifico."""
    aluno = Aluno.objects.filter(pk=aluno_id)

    aluno_json = serializers.serialize("json", aluno)

    return HttpResponse(aluno_json , content_type="application/json")

