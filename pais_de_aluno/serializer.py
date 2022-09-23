from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response
from pais_de_aluno.models import Pais_aluno

class Pais_alunoSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Pais_aluno
        fields = "_all_"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["urls", "username", "first_name", "last_name"]

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        write_only=True,
          required=True,
          style={"input_type": "password", "placeholder": "password"},
    )

    class Meta:
        model = get_user_model()
        fields = [
            "url",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        ]
        extra_kwarg = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data["password"] = make_password(
            validated_data.get("password")
        )
        return super(CreateUserSerializer, self).create(validated_data)
    
class Pais_alunoSerializer(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer(required=True)
    
    
    class Meta:
        model = Pais_aluno
        fields = [
            "url",
            "user",
            "filho",
            "cpf",
            "born",
            "endereco",
            "telefone",
            "rg",
        ]

        def create(self, validated_data):
            user_data = validated_data.pop("user")
            user = CreateUserSerializer.create(
                CreateUserSerializer(), validated_data=user_data)
            if user.pk:
                pai,created = Pais_aluno.objects.update_or_create(
                    user = user,
                    filho = validated_data.pop("filho"),
                    cpf = validated_data.pop("cpf"),
                    born = validated_data.pop("born"),
                    endereco = validated_data.pop("endereco"),
                    telefone = validated_data.pop("telefone"),
                    rg = validated_data.pop("rg"),

                )
                if created:
                    return pai
            else:
                user.delete()
            return Response(
                {"message": "Não pude criar um novo responsavel"}, status=406
            )
            