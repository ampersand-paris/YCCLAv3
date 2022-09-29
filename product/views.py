from django.shortcuts import render
from product.models import Product

# Create your views here.

def product_index_view(request):
        
    products = Product.objects.all().filter(is_available=True)
   
    context = {
        'products' : products,
    }

    return render(request, 'index.html', context)
