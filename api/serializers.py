from rest_framework import serializers

from .models import Endereco
from .models import Cliente
from .models import Produto
from .models import Pedido


class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Endereco
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedido
        fields = '__all__'
