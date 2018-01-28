from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Product, Add
from .serializers import ProductSerializer

class ProductViewSet(ViewSet):

	def get(self, request, category= None):

		""" Get all products or filter """

		if category:
			try:
				products = Product.objects.filter(category__name= category)
			except Exception as e:
				return Response({'message':'Invalid category'}, code= 404)
		else:
			products = Product.objects.all()

		product_output = ProductSerializer(products, many= True).data

		return Response({'products':product_output})
