from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    store,
    product_detail,
)

app_name = "ycclav3"

urlpatterns = [
    path('', store, name='store'),
    path('<slug:category_slug>/', store, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail')
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)