
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("aluno/", include("aluno.urls")),
    path('professor/', include("professor.urls")),
    path("egresso/", include("egresso.urls")),
    path("pais_de_aluno/", include("pais_de_aluno.urls")),
    path("curso/", include("curso.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
