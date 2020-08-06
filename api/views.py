from rest_framework import permissions, viewsets

from .models import Cliente, Endereco, Pedido, Produto
from .serializers import (ClienteSerializer, EnderecoSerializer,
                          PedidoSerializer, ProdutoSerializer)

# Create your views here.


class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (permissions.AllowAny, )


class EnderecoViewSet(viewsets.ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Endereco.objects.filter(cliente=self.kwargs["cliente_pk"])


class ProdutosViewSet(viewsets.ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class ProdutoViewSet(viewsets.ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return Produto.objects.filter(pedido=self.kwargs["pedido_pk"])


class PedidoViewSet(viewsets.ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
