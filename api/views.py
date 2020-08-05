from rest_framework import viewsets

from .models import Cliente
from .serializers import ClienteSerializer

from .models import Endereco
from .serializers import EnderecoSerializer

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EnderecoViewSet(viewsets.ModelViewSet):

    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
