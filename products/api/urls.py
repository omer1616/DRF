#from rest_framework.urls import  path

from django.urls import path
from .views import product_list_and_create_api_view


urlpatterns = [
    path('category/', product_list_and_create_api_view, name='category'),
    # path('category/<int:pk>', category_list_and_create_api_view, name='category_detail')
]