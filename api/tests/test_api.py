from django.urls import reverse
from rest_framework.test import APILiveServerTestCase

# Create your tests here.


class TestSetUp(APILiveServerTestCase):
    """Testado o registro do token para o user..."""

    def setUp(self):
        self.login_url = reverse("api:cliente-list")
        self.token_url = reverse("api:token")
        self.user_data = {
            "nome": "user",
            "sobrenome": "user",
            "cpf": "680.494.740-11",
            "rg": "9999",
            "telefone": "+5599999999999",
            "endereco": "490000",
            "username": "user",
            "email": "user@provider.com",
            "password": "somepassword",
            "aniversario": "2001-01-01",
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
