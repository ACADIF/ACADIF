from django.contrib.auth import get_user_model
from rest_framework import viewsets
from aluno.models import Aluno

from aluno.serializers import (
    UserSerializer,
    AlunoSerializer,
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
