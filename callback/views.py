from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import CallBack


class CallBackViewSet(ViewSet):

	def post(self, request):

		name = request.data['name'] if 'name' in request.data else None
		phone = request.data['cell'] if 'cell' in request.data else None

		print(request.data)

		if not (name and phone):
			return Response({'message':'Invalid data'}, status= 400)
		CallBack(name= name, phone= phone).save()
		return Response({'message':'success'})
