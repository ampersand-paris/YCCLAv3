from django.db import models
from category.models import Category
# Create your models here.

class Product(models.Model):

    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    recipe_authors = models.CharField(max_length=100)
    illustrators = models.CharField(max_length=100)
    price = models.IntegerField()
    images = models.ImageField(upload_to="photos/products")
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    primary_color = models.CharField(max_length=100, default="var(--main-blue)")
    secondary_color = models.CharField(max_length=100, default="var(--main-red)")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name