from rest_framework import serializers

from .models import Cliente
from .models import Endereco
from .models import Produto
from .models import Pedido

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ('nome', 'sobrenome', 'cpf', 'rg', 'telefone', 'email')

class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Endereco
        fields = ('logradouro', 'tipo', 'numero', 'bairro', 'cidade', 'estado', 'cliente')


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produto
        fields = ('produto', 'preco', 'estoque')

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ('quantidade',)
