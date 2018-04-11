from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Subscriber


class SubscriberViewSet(ViewSet):

	def post(self, request):
		""" Create new subscriber """
		email = request.data['email'] if 'email' in request.data else None

		if email:
			subscriber, is_created = Subscriber.objects.get_or_create(email= email)
			if is_created:
				subscriber.save()
			return Response({'message':'success'})
		return Response({'message':'Invalid email'}, status= 400)