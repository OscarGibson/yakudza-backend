from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Tag
from .serializers import TagSerializer

class TagViewSet(ViewSet):
	""" Get tags list """

	def get(self, request):
		tag = Tag.objects.all()
		tag_output = TagSerializer(tag, many= True).data
		return Response({'tags':tag_output})