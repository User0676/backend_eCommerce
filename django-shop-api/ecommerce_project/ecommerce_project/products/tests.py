from django.test import TestCase
from .models import Product, Category

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Smartphone",
            description="A modern smartphone",
            price=699.99,
            stock_quantity=50,
            category=self.category
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Smartphone")
        self.assertEqual(self.product.price, 699.99)
        self.assertEqual(self.product.stock_quantity, 50)

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
