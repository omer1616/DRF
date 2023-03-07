#from rest_framework.urls import  path

from django.urls import path
from .views import category_list_and_create_api_view


urlpatterns = [
    path('category/', category_list_and_create_api_view, name='category')
]