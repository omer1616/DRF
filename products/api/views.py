from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.models import Category
from products.api.serializers import CategorySerializer

@api_view(['GET', 'POST'])
def product_list_and_create_api_view(request):
    if request.method == "GET":
        category = Category.objects.filter(is_active=True)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)