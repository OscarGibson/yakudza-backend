from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import FeedbackSerializer
from .models import Feedback


class FeedbackViewSet(ViewSet):

	def get(self, request):
		feedback = Feedback.objects.all()
		feedback_out = FeedbackSerializer(feedback, many= True).data
		return Response({'feedbacks':feedback_out})

	def post(self, request):
		print(request.data)
		author = request.data['author'] if 'author' in request.data else None
		phone = request.data['cell'] if 'cell' in request.data else None
		content = request.data['content'] if 'content' in request.data else None

		if not (author and content):
			return Response({'message':'Invalid data'}, status= 400)
		Feedback(author= author, phone= phone, content= content).save()
		return Response({'message':'success'})
