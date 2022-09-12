"""URLS paths do PROFESSOR"""
from django.urls import path
from professor import views

urlpatterns = [
    path("", views.get_professores, name="get_professor"),
    path("add/", views.post_professor, name="post_professor"),
    path("remove/<professor_id>/", views.delete_professor, name="delete_professor"),
]