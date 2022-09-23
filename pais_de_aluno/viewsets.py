from django.contrib.auth import get_user_model
from rest_framework import viewsets
from pais_de_aluno.models import Pais_aluno

from pais_de_aluno.serializer import (
    UserSerializer,
    Pais_alunoSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class pais_alunoViewSet(viewsets.ModelViewSet):
    queryset = Pais_aluno.objects.all()
    serializer_class = Pais_alunoSerializer
