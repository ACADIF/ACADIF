"""URLS paths do aluno"""
from django.urls import path, include
from pais_de_aluno import views
from rest_framework import routers
from pais_de_aluno.viewsets import (
    pais_alunoViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register(r"users",UserViewSet)
router.register(r"pai_de_alunos",pais_alunoViewSet)


urlpatterns = [
    path("", views.get_pais_aluno, name="get_pais_aluno"),
    path("add/", views.post_pais_aluno, name="post_pais_aluno"),
    path("get/<aluno_id>/", views.get_pai, name="get_pai"),
    path("remove/<pais_id>/", views.delete_pai, name="delete_pai"),
    path("api/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
