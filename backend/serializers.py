from rest_framework import serializers
from .models import Company


class RegionSerializer(serializers.Serializer):
    Region = serializers.CharField()


class LocalitySerializer(serializers.Serializer):
    Locality = serializers.CharField()


class CategoriesSerializer(serializers.Serializer):
    Categories = serializers.CharField()


class ProductsSerializer(serializers.Serializer):
    Products = serializers.CharField()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
