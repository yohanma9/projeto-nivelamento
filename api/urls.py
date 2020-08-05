from django.urls import path
from django.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import ClienteViewSet
from .views import EnderecoViewSet
from .views import ProdutoViewSet
from .views import PedidoViewSet

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'pedido', PedidoViewSet)

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
