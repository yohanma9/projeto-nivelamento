from django.db import models

from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

# Create your models here.

class Cliente(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE_CASCADE

    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    cpf = CPFField('CPF', unique=True)
    rg = models.CharField('RG', max_length=100, unique=True)
    telefone = PhoneNumberField('Telefone')
    email = models.EmailField('Email', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nome} - {self.email}'

class Endereco(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE_CASCADE

    ESTADOS = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]

    TIPOS = [
        ('Principal', 'Principal'),
        ('Secundário', 'Secundário'),
    ]

    logradouro = models.CharField('Logradouro', max_length=100)
    numero = models.PositiveIntegerField('Número')
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100, choices=ESTADOS)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    tipo = models.CharField('Tipo', max_length=100, choices=TIPOS)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f'{self.logradouro} - {self.numero}'


class Produto(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE_CASCADE

    produto = models.CharField('Produto', max_length=100)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField('Estoque')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.produto} - {self.estoque}'

class Pedido(SafeDeleteModel):

    _safedelete_policy = SOFT_DELETE_CASCADE

    quantidade = models.PositiveIntegerField('Quantidade')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'{self.quantidade}'
