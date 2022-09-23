"""Testes da aplicação professor"""
from django.test import TestCase
import json
from django.utils import timezone
from django.contrib.auth import get_user_model
from professor.models import Professor, Titulo

class ProfessorTestCase(TestCase):
    def setUp(self):
        
        user1 = get_user_model().objects.create(
            username="zeza", email="zeza@dosteclados.com", password="1234567"
        )
        titulo = Titulo.objects.create(formacao = "ciencias", grau = "B", instituicao = "IFCE")
        Professor.objects.create(user = user1, CPF = 123, BORN = "2012-12-20", ENDERECO = "aracati", SALARIO = 10000, TITULO = titulo)
    def tests_retorna_200_post(self):
        user0 = get_user_model().objects.create(
            username="zezo", email="zezo@dosteclados.com", password="123456"
        )
        titulo0 = Titulo.objects.create(formacao = "ciencias", grau = "B", instituicao = "IFCE")
        response = self.client.post(
            "/professor/add/",
            data={
                "user": user0 , "TITULO" : titulo0 , "CPF" : 1234, "BORN" : timezone.now, "ENDERECO" : "cascavel", "SALARIO" : 10000,   
            },
        )
        self.assertEqual(response.status_code, 200)
    
