from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('products/<slug:category>', detail_products, name='products'),
    path('filter', filter_view, name='filter')
]
