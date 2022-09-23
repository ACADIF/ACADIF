"""URLS paths do aluno"""
from django.urls import path, include
from aluno import views
from rest_framework import routers
from aluno.viewsets import (
    AlunoViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register(r"users",UserViewSet)
router.register(r"alunos",AlunoViewSet)


urlpatterns = [
    path("", views.get_Alunos, name="get_Aluno"),
    path("add/", views.post_Aluno, name="post_Aluno"),
    path("remove/<Aluno_matricula>/", views.delete_Aluno, name="delete_Aluno"),
<<<<<<< Updated upstream
]
=======
    path("api/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
>>>>>>> Stashed changes
