"""URLS paths do aluno"""
from django.urls import path
from aluno import views

urlpatterns = [
    path("", views.get_Alunos, name="get_Alunos"),
    path("add/", views.post_Aluno, name="post_Aluno"),
    path("get/<aluno_id>/", views.get_aluno, name="get_Aluno"),
    path("remove/<Aluno_matricula>/", views.delete_Aluno, name="delete_Aluno"),
]
