from django.urls import path

from .views import (
    products_list_view,
    products_create_view
)

app_name = 'products'
urlpatterns = [
    path('', products_list_view, name='products_list'),
    path('create/', products_create_view, name='products_create')
]
