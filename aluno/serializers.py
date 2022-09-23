from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.response import Response
from aluno.models import Aluno

class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Aluno
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
    
class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    user = CreateUserSerializer(required=True)
    
    
    class Meta:
        model = Aluno
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
                aluno,created = Aluno.objects.update_or_create(
                    user = user,
                    matricula = validated_data.pop("matricula"),
                    cpf = validated_data.pop("cpf"),
                    born = validated_data.pop("born"),
                    endereco = validated_data.pop("endereco"),
                    nome_pai = validated_data.pop("nome_pai"),
                    nome_mae = validated_data.pop("nome_mae"),
                    sexo = validated_data.pop("sexo"),
                    telefone = validated_data.pop("telefone"),
                    estado_civil = validated_data.pop("estado_civil"),
                    rg = validated_data.pop("rg"),

                )
                if created:
                    return aluno
            else:
                user.delete()
            return Response(
                {"message": "Não pude criar um novo aluno"}, status=406
            )
            