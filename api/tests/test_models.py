from django.test import TestCase
from model_bakery import baker

# Create your tests here.

baker.generators.add("cpf_field.models.CPFField",
                     "model_bakery.random_gen.gen_string")
baker.generators.add(
    "phonenumber_field.modelfields.PhoneNumberField",
    "model_bakery.random_gen.gen_string",
)


class EnderecoTestCase(TestCase):
    """Testando o modelo endedereço..."""

    def setUp(self):
        self.endereco = baker.make("Endereco")

    def test_str(self):
        self.assertEqual(str(self.endereco), self.endereco.logradouro)


class ClienteTestCase(TestCase):
    """Testando o modelo cliente..."""

    def setUp(self):
        self.cliente = baker.make("Cliente")

    def test_str(self):
        self.assertEqual(str(self.cliente), self.cliente.nome)


class ProdutoTestCase(TestCase):
    """Testando o modelo produto..."""

    def setUp(self):
        self.produto = baker.make("Produto")

    def test_str(self):
        self.assertEqual(str(self.produto), self.produto.produto)


class PedidoTestCase(TestCase):
    """Testando o modelo pedido..."""

    def setUp(self):
        self.pedido = baker.make("Pedido")

    def test_str(self):
        self.assertEqual(float(str(self.pedido)), self.pedido.valor)
