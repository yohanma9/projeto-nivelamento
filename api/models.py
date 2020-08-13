import uuid

from cpf_field.models import CPFField
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from safedelete.models import SOFT_DELETE_CASCADE, SafeDeleteModel

from .managers import ClienteManager

# Create your models here.


class Endereco(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE_CASCADE

    ESTADOS = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logradouro = models.CharField("Logradouro",
                                  max_length=100,
                                  null=False,
                                  blank=False)
    numero = models.PositiveIntegerField("Número", null=False, blank=False)
    complemento = models.CharField("Complemento",
                                   max_length=100,
                                   null=False,
                                   blank=False)
    bairro = models.CharField("Bairro",
                              max_length=100,
                              null=False,
                              blank=False)
    cidade = models.CharField("Cidade",
                              max_length=100,
                              null=False,
                              blank=False)
    estado = models.CharField("Estado",
                              max_length=100,
                              choices=ESTADOS,
                              null=False,
                              blank=False)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.logradouro}"


class Cliente(SafeDeleteModel, AbstractUser):

    _safedelete_policy = SOFT_DELETE_CASCADE

    SEXO = (("F", "Feminino"), ("M", "Masculino"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField("Nome", max_length=100, null=False, blank=False)
    sobrenome = models.CharField("Sobrenome",
                                 max_length=100,
                                 null=False,
                                 blank=False)
    aniversario = models.DateField("Aniversário", null=False, blank=False)
    cpf = CPFField("CPF", unique=True, null=False, blank=False)
    rg = models.CharField("RG",
                          max_length=100,
                          unique=True,
                          null=False,
                          blank=False)
    telefone = PhoneNumberField("Telefone", null=False, blank=False)
    email = models.EmailField("Email",
                              max_length=100,
                              unique=True,
                              null=False,
                              blank=False)
    endereco = models.CharField("Endereço",
                                max_length=100,
                                null=False,
                                blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "aniversario"]

    objects = ClienteManager()

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nome}"


class Produto(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE_CASCADE

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    produto = models.CharField("Produto",
                               max_length=100,
                               null=False,
                               blank=False)
    descricao = models.CharField("Descrição",
                                 max_length=200,
                                 null=False,
                                 blank=False)
    preco = models.FloatField("Preço", null=False, blank=False)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return f"{self.produto}"


class Pedido(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE_CASCADE

    STATUS = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey("Cliente",
                                on_delete=models.CASCADE,
                                related_name="pedidos")
    observacoes = models.CharField("Observações",
                                   max_length=300,
                                   null=False,
                                   blank=False)
    data = models.DateField("Data", null=False, blank=False)
    valor = models.FloatField("Valor", blank=False, null=False)
    status = models.CharField("Status",
                              max_length=1,
                              choices=STATUS,
                              blank=False,
                              null=False)
    produtos = models.ManyToManyField(Produto)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"{self.valor}"
