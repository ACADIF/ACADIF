from django.urls import path, include
from curso import views
from rest_framework import routers
from curso.viewsets import (CursoViewSet,)

router = routers.DefaultRouter()
router.register(r"cursos",CursoViewSet)

urlpatterns = [
    path("", views.get_Cursos, name="get_Curso"),
    path("add/", views.post_Curso, name="post_Curso"),
    path("get/<aluno_id>/", views.get_Curso, name="get_Curso"),
    path("remove/<Aluno_matricula>/", views.delete_Curso, name="delete_Curso"),
    path("api/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
