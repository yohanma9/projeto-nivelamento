from django.urls import path
from django.urls import include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .views import EnderecoViewSet
from .views import ClienteViewSet
from .views import ProdutoViewSet
from .views import PedidoViewSet

router = routers.DefaultRouter()
router.register(r'endereco', EnderecoViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'pedido', PedidoViewSet)

urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/',
        jwt_views.TokenRefreshView.as_view(), name='refresh')
]
