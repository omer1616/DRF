from rest_framework import serializers
from ..models import *


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    created_date = serializers.DateTimeField(read_only=True)
    relase_date = serializers.DateField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.relase_date = validated_data.get('relase_date', instance.relase_date)
        instance.is_active = validated_data.get('is_activate', instance.is_active)
        instance.save()
        return instance
