from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename='order')
router.register('order-items', OrderItemViewSet, basename='orderitem')

urlpatterns = [
    path('', include(router.urls)),
]
