from rest_framework import serializers
from .models import Wishlist, WishlistItem

class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ['id', 'wishlist', 'product', 'created_at']

class WishlistSerializer(serializers.ModelSerializer):
    items = WishlistItemSerializer(many=True, read_only=True, source='wishlistitem_set')

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'created_at', 'updated_at', 'items']
