#from rest_framework.urls import  path

from django.urls import path
from .views import product_list_and_create_api_view, product_detail_api_view


urlpatterns = [
    path('products/', product_list_and_create_api_view, name='product'),
    path('products/<int:pk>', product_detail_api_view, name='product_detail')
]