from django.contrib import admin
from aluno.models import Aluno
from disciplina.models import disciplina
from turma.models import turma_semestre
# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "foto_perfil"
    ]

    search_fields = ["user_username"]
    ordering = ["user"]

admin.site.register(turma_semestre)
admin.site.register(Aluno)
admin.site.register(disciplina)