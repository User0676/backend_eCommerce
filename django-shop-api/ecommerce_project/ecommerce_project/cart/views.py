from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import ShoppingCart, CartItem
from .serializers import ShoppingCartSerializer, CartItemSerializer
from django.conf import settings
from rest_framework.decorators import action
from products.models import Product

class ShoppingCartViewSet(viewsets.GenericViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def mine(self, request):
        # Возвращаем корзину текущего пользователя, если нет - создаем
        cart, created = ShoppingCart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def create(self, request, *args, **kwargs):
        # При добавлении товара проверяем, есть ли у пользователя корзина
        cart, _ = ShoppingCart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # Проверяем, есть ли уже такой товар в корзине
        quantity = int(request.data.get('quantity', 1))

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
