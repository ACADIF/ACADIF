from tkinter import E
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response
from egresso.models import Egresso
from aluno.serializers import CreateUserSerializer

class EngressoSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Egresso
        fields = "_all_"

class EngressoSerializer(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer()

    class Meta:
        model = Egresso
        fields = [
            "url",
            "user",
            "matricula",
            "cpf",
            "born",
            "endereco",
            "nome_pai",
            "nome_mae",
            "sexo",
            "telefone",
            "estado_civil",
            "rg",
        ]
        def create(self, validated_data):
            user_data = validated_data.pop("user")
            user = CreateUserSerializer.create(
                CreateUserSerializer(), validated_data=user_data)
            if user.pk:
                egresso,created = Egresso.objects.update_or_create(
                    user = user,
                    matricula = validated_data.pop("matricula"),
                    cpf = validated_data.pop("cpf"),
                    born = validated_data.pop("born"),
                    endereco = validated_data.pop("endereco"),
                    estado = validated_data.pop("estado_civil"), 
                    nome_pai = validated_data.pop("nome_pai"),
                    nome_mae = validated_data.pop("nome_mae"),
                    sexo = validated_data.pop("sexo"),
                    telefone = validated_data.pop("telefone"),
                    estado_civil = validated_data.pop("estado_civil"),
                    rg = validated_data.pop("rg"),
                )
                if created:
                    return egresso
            else:
                user.delete()
            return Response(
                {"message": "Não pude criar um novo egresso"}, status=406
            )
            