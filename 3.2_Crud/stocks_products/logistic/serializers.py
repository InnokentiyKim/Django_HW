from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            values = {'price': position.get('price'), 'quantity': position.get('quantity')}
            StockProduct.objects.update_or_create(defaults=values, stock=stock, **position)
        return stock


    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position in positions:
            updating_values = {'product': position.get('product'), 'price': position.get('price'), 'quantity': position.get('quantity')}
            StockProduct.objects.update_or_create(defaults=updating_values, stock=stock, product=position.get('product'))
        return stock
