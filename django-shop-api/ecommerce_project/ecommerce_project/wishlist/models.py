from django.db import models
from django.conf import settings
from products.models import Product


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # индекс есть
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE) # индекс есть
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # индекс есть
    created_at = models.DateTimeField(auto_now_add=True)
