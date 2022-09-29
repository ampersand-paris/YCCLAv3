from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import (
    product_index_view,
)

app_name = "ycclav3"

urlpatterns = [
    path('', product_index_view, name='collections'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)