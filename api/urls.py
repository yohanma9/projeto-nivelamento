from django.urls import path
from django.urls import include
from rest_framework import routers

from .views import ClienteViewSet
from .views import EnderecoViewSet


router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet)
router.register(r'endereco', EnderecoViewSet)

urlpatterns = [
    path('api/', include(router.urls))

]
