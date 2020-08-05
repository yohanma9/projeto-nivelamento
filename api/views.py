from rest_framework import viewsets
from rest_framework import permissions

from .models import Cliente
from .serializers import ClienteSerializer

from .models import Endereco
from .serializers import EnderecoSerializer

from .models import Produto
from .serializers import ProdutoSerializer

from .models import Pedido
from .serializers import PedidoSerializer

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (permissions.IsAuthenticated,)

class EnderecoViewSet(viewsets.ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ProdutoViewSet(viewsets.ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (permissions.IsAuthenticated,)

class PedidoViewSet(viewsets.ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (permissions.IsAuthenticated,)
