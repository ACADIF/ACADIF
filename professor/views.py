"""Views do professor"""
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.http import require_http_methods
from professor.models import Professor

@require_http_methods(["POST"])
def post_professor(request):
    """Adiciona um ALUNO."""
    nova = Professor()
    nova.NOME = request.POST["NOME"]
    nova.CPF = request.POST["CPF"]
    nova.BORN = request.POST["BORN"]
    nova.ENDERECO = request.POST["ENDERECO"]
    nova.SALARIO = request.POST["SALARIO"]
    nova.save()
    return HttpResponse("Professor salvo")


@require_http_methods(["GET"])
def get_professores(request):
    """retorna os dados de todos os professor"""
    professor = Professor.objects.all()
    resp_json = serializers.serialize("json", professor)

    return HttpResponse(resp_json, content_type="application/json")

@require_http_methods(["DELETE"])
def delete_professor(request, professor_id):
    post = Professor.objects.get(pk=professor_id)
    post.delete()

    return HttpResponse("Deletado com Sucesso.")