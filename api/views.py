from rest_framework import viewsets
from rest_framework import permissions

from .models import Cliente
from .serializers import ClienteSerializer

from .models import Endereco
from .serializers import EnderecoSerializer

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (permissions.IsAuthenticated,)

class EnderecoViewSet(viewsets.ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = (permissions.IsAuthenticated,)
