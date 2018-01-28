from rest_framework.serializers import ModelSerializer
from .models import Product

class ProductSerializer(ModelSerializer):
	""" Product serializer """
	class Meta:
		model = Product
		fields = '__all__'

class ProductSerializerMini(ModelSerializer):
	""" Product serializer """
	class Meta:
		model = Product
		fields = ('id', 'title', 'description', 'image', 'price', 'weight', 'kkal')