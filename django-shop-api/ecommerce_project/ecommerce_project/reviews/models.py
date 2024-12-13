from django.db import models
from django.conf import settings
from products.models import Product


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # индекс есть
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # индекс есть
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
