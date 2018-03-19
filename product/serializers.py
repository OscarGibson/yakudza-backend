from rest_framework import serializers
from .models import Product, Labels

class LabelSerializer(serializers.ModelSerializer):
	""" Serializer for product label """
	class Meta:
		model = Labels
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
	""" Product serializer """
	label_serializer = serializers.SerializerMethodField('_get_labels', read_only= True)

	def _get_labels(self, obj):
		return LabelSerializer(obj.label, many= True).data

	class Meta:
		model = Product
		extra_fields = ('label_serializer',)
		exclude = ('label',)

class ProductSerializerMini(serializers.ModelSerializer):
	""" Product serializer """
	class Meta:
		model = Product
		fields = ('id', 'title', 'description', 'image', 'price', 'weight', 'pieces')