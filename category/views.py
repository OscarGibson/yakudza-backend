from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(ViewSet):
	""" Get categoies with nested products """

	def get(self, request):
		categories = Category.objects.all()
		categories_output = CategorySerializer(categories, many= True).data
		return Response({'categories':categories_output})