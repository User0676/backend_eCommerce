from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShoppingCartViewSet, CartItemViewSet

router = DefaultRouter()
router.register('cart-items', CartItemViewSet, basename='cartitem')

urlpatterns = [
    path('cart/', ShoppingCartViewSet.as_view({'get': 'mine'}), name='shopping_cart'),
    path('', include(router.urls)),
]
