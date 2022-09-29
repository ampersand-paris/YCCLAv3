from django.urls import path

from .views import (
    cart,
)

app_name = "ycclav3"

urlpatterns = [
    path('', cart, name="cart")
]