<<<<<<< branch_rondy
<<<<<<< Updated upstream
from django.test import TestCase

# Create your tests here.
=======
=======
>>>>>>> local
"""Testes da aplicação Aluno"""
from django.test import TestCase
import json
from aluno.models import Aluno

class AlunoTestCase(TestCase):
    def setUp(self):
        Aluno.objects.create(nome="rondinele", mat=123)

    def tests_post_retorna_405_para_http_nao_post(self):
        response = self.client.get("/aluno/add/")
        self.assertEqual(response.status_code, 405)
    
    def tests_Aluno_retorna_200_para_post(self):
        response = self.client.post(
            "/aluno/add/",
            data={
                "nome": "rondinele", "mat": 123,
            },
        )
        existe = Aluno.objects.filter(mat=123)

        self.assertEqual(len(existe),1)
        self.assertEqual(response.status_code, 200)
    
    def tests_get_Aluno_especifico(self):
            response = self.client.get("/aluno/get/1/")

            resp_dict = json.loads(response.content)

            self.assertTrue(
                resp_dict[0]["fields"]["nome"]
                == "rondinele"
            )


    def tests_delete_Aluno(self):
        response_delete = self.client.delete("/aluno/remove/123/")

        self.assertEqual(response_delete.status_code, 200)
>>>>>>> Stashed changes
