import requests.cookies

from products.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from products.api.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list_and_create_api_view(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)



    elif requests.method == "PUT":
        pass
