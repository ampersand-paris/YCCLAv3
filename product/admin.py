from django.contrib import admin
from product.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'recipe_authors', 'illustrators', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields={'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)
