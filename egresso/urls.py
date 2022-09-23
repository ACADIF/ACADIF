from django.urls import path, include
from aluno import views
from rest_framework import routers
from egresso.viewsets import (
    EgressoViewSet
)

router = routers.DefaultRouter()
router.register(r"engresso",EgressoViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]