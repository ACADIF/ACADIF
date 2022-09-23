from django.contrib.auth import get_user_model
from rest_framework import viewsets
from egresso.models import Egresso

from egresso.serializers import (
    EngressoSerializer
)

class EgressoViewSet(viewsets.ModelViewSet):
    queryset = Egresso.objects.all()
    serializer_class = EngressoSerializer