from rest_framework import serializers
from .models import Product, Stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['quantity', 'last_updated']

class ProductSerializer(serializers.ModelSerializer):
    stock = StockSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'short_description', 'product_description', 'price', 'stock']

    def create(self, validated_data):
        stock_data = validated_data.pop('stock')
        # First create the product
        product = Product.objects.create(**validated_data)
        # Then create the stock with the product as foreign key
        Stock.objects.create(product=product, **stock_data)
        return product

    def update(self, instance, validated_data):
        stock_data = validated_data.pop('stock', None)

        # Update product fields
        instance.name = validated_data.get('name', instance.name)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.product_description = validated_data.get('product_description', instance.product_description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        # Update stock if provided
        if stock_data:
            stock = instance.stock
            stock.quantity = stock_data.get('quantity', stock.quantity)
            stock.save()

        return instance
