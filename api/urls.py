from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OperadoraViewSet, api_root

router = DefaultRouter()
router.register(r'operadoras', OperadoraViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]
