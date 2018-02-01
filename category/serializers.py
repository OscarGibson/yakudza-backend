from rest_framework import serializers
from product.models import Product
from product.serializers import ProductSerializer
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
	""" Category serializer """

	products = serializers.SerializerMethodField('_get_products', read_only= True)

	def _get_products(self, obj):
		return ProductSerializer(
			Product.objects.filter(categories= obj), many= True
			).data

	class Meta:
		model = Category
		fields = ('id', 'name', 'slug', 'products')