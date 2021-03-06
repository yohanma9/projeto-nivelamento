from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt import views as jwt_views

from .views import (ClienteViewSet, EnderecoViewSet, PedidoViewSet,
                    ProdutosViewSet, ProdutoViewSet)

app_name = "api"

router = routers.SimpleRouter()

router.register(r"pedidos", PedidoViewSet)
pedidos_router = routers.NestedSimpleRouter(router,
                                            r"pedidos",
                                            lookup="pedido")
pedidos_router.register(r"produtos", ProdutoViewSet)

router.register(r"clientes", ClienteViewSet)
clientes_router = routers.NestedSimpleRouter(router,
                                             r"clientes",
                                             lookup="cliente")
clientes_router.register(r"enderecos", EnderecoViewSet)

router.register(r"produtos", ProdutosViewSet)

urlpatterns = [
    path("", include(router.urls), name="produtos"),
    path("", include(pedidos_router.urls), name="pedidos"),
    path("", include(clientes_router.urls), name="clientes"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/",
         jwt_views.TokenRefreshView.as_view(),
         name="refresh"),
]
