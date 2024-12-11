from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WishlistViewSet, WishlistItemViewSet

router = DefaultRouter()
router.register('wishlist-items', WishlistItemViewSet, basename='wishlistitem')

urlpatterns = [
    path('wishlist/', WishlistViewSet.as_view({'get': 'mine'}), name='my_wishlist'),
    path('', include(router.urls)),
]
