from rest_framework import viewsets
from curso.models import Curso
from curso.serializer import (CursoSerializer)

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer