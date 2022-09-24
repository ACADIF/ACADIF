"""URLS paths do aluno"""
from django.urls import path
from aluno import views

urlpatterns = [
    path("", views.get_Alunos, name="get_Aluno"),
    path("add/", views.post_Aluno, name="post_Aluno"),
    path("remove/<Aluno_matricula>/", views.delete_Aluno, name="delete_Aluno"),
]