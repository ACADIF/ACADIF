"""Views dos pais"""
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from aluno.models import Aluno
from pais_de_aluno.viewsets import pais_alunoViewSet
from pais_de_aluno.models import Pais_aluno

@require_http_methods(["GET"])
def get_pais_aluno(request):
    """Retorna os dados de todos os aluno"""
    pais = Pais_aluno.objects.all()
    resp_json = serializers.serialize("json", pais)
    return HttpResponse (resp_json, content_type="application/json")

@require_http_methods(["POST"])
def post_pais_aluno(request):
    """Adiciona um ALUNO."""
    nova = Pais_aluno()
    nova.user = get_user_model().objects.get(pk=request.POST["user_id"])
    nova.filho = Aluno.objects.get(pk = request.POST["matricula"])
    nova.cpf = request.POST["cpf"]
    nova.born = request.POST["born"]
    nova.endereco = request.POST["endereco"]
    nova.telefone = request.POST["telefone"]
    nova.rg =  request.POST["rg"]
    nova.save()
    return HttpResponse("pai salvo com sucedida")

@require_http_methods(["DELETE"])
def delete_pai(request, pais_id):
    post = Pais_aluno.objects.get(pk=pais_id)
    post.delete()

    return HttpResponse("Deletado com sucesso.")

@require_http_methods(["GET"])
def get_pai(request, pais_id):
    """Retorna aluno especifico."""
    aluno = Pais_aluno.objects.filter(pk=pais_id)

    aluno_json = serializers.serialize("json", aluno)

    return HttpResponse(aluno_json , content_type="application/json")

