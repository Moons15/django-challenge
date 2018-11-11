from apps.product.models import Product, ProductDetail
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'is_variation', 'brand_id', 'code',
                  'family', 'is_complement', 'is_delete')

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            brand_id=validated_data['brand_id'],
            code=validated_data['code'],
            family=validated_data['family'],
            is_complement=validated_data['is_complement'],
            is_delete=validated_data['is_delete'],
            is_variation=validated_data['is_variation'],
        )
        return product


class CRUDProductSerializer(serializers.ModelSerializer):
    type = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    brand_id = serializers.IntegerField(required=False)
    code = serializers.IntegerField(required=False)
    family = serializers.IntegerField(required=False)
    class Meta:
        model = Product
        exclude = ('created', 'modified')


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
