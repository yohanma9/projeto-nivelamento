from rest_framework import serializers

from .models import Cliente
from .models import Endereco

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ('nome', 'sobrenome', 'cpf', 'rg', 'telefone', 'email')

class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Endereco
        fields = ('logradouro', 'numero', 'bairro', 'cidade', 'estado', 'cliente')
