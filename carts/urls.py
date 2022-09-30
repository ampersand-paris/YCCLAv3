from django.urls import path

from .views import (
    cart,
    add_cart,
    subtract_cart,
    remove_cart_item,
)

app_name = "ycclav3"

urlpatterns = [
    path('', cart, name="cart"),
    path('add_cart/<int:product_id>/', add_cart, name="add_cart"),
    path('subtract_cart/<int:product_id>/', subtract_cart, name="subtract_cart"),
    path('remove_cart_item/<int:product_id>/', remove_cart_item, name="remove_cart_item"),
]