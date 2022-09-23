from rest_framework import serializers
from rest_framework.response import Response
from curso.models import Curso

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Curso
        fields = "_all_"

class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = [
            "url",
            "nome",
            "matriz_curricular",
            "data_vigor"
        ]

        def create(self, validated_data):
            curso, created = Curso.objects.update_or_create(
                nome = validated_data.pop("nome"),
                matriz_curricular = validated_data.pop("matriz_curricular"),
                data_vigor = validated_data.pop("data_vigor"),
            )
            if created:
                return curso
            else:
                return Response(
                    {"message": "Não pude criar o curso"}, status=406
                )
    