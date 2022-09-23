from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from egresso.models import Engresso

@require_http_methods(["GET"])
def get_Engressos(request):
    engresso = Engresso.objects.all()
    resp_json = serializers.serialize("json", Engresso)
    return HttpResponse(resp_json, content_type="application/json")


@require_http_methods(["POST"])
def post_Engressos(request):
    """Adiciona um ALUNO."""
    nova = Engresso()
    nova.user = get_user_model().objects.get(pk=request.POST["user_id"])
    nova.matricula = request.POST["matricula"]
    nova.cpf = request.POST["cpf"]
    nova.born = request.POST["born"]
    nova.endereco = request.POST["endereco"]
    nova.estado_civil = request.POST["estado_civil"]
    nova.telefone = request.POST["telefone"]
    nova.nome_pai = request.POST["nome_pai"]
    nova.nome_mae = request.POST["nome_mae"]
    nova.sexo = request.POST["sexo"]
    nova.rg =  request.POST["rg"]
    nova.save()
    return HttpResponse("Engresso salvo com sucedida")

@require_http_methods(["DELETE"])
def delete_Engresso(request, engresso_matricula):
    post = Engresso.objects.get(pk=engresso_matricula)
    post.delete()

    return HttpResponse("Deletado com sucesso.")

@require_http_methods(["GET"])
def get_aluno(request, engresso_id):
    """Retorna aluno especifico."""
    aluno = Engresso.objects.filter(pk=engresso_id)

    aluno_json = serializers.serialize("json", aluno)

    return HttpResponse(aluno_json , content_type="application/json")

