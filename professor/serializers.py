from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response
from professor.models import Professor
from aluno.serializers import CreateUserSerializer

class ProfessorSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields = "_all_"

class CreateProfessor(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer()

    class Meta:
        model = Professor
        fields = [
            "url",
            "user",
            "CPF",
            "BORN",
            "ENDERECO",
            "SALARIO",
            "TITULO",
        ]
        def create(self, validated_data):
            user_data = validated_data.pop("user")
            user = CreateUserSerializer.create(
                CreateUserSerializer(), validated_data=user_data
            )
            if user.pk:
                professor,created = Professor.objects.update_or_create(
                    user = user,
                    CPF = validated_data.pop("CPF"),
                    BORN = validated_data.pop("BORN"),
                    ENDERECO = validated_data.pop("ENDERECO"),
                    SALARIO = validated_data.pop("SALARIO"),
                    TITULO = validated_data.pop("TITULO"),
                )
                if created:
                    return professor
            else:
                user.delete()
            return Response({"message": "Não pude criar um novo aluno"}, status=406)
