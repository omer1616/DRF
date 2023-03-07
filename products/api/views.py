from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import *
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
