from rest_framework import serializers
from .models import ShoppingCart, CartItem
from products.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product_detail = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'created_at', 'updated_at', 'product_detail']

    def get_product_detail(self, obj):
        return {
            "name": obj.product.name,
            "price": str(obj.product.price)
        }


class ShoppingCartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True, source='cartitem_set')

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'created_at', 'updated_at', 'items']
