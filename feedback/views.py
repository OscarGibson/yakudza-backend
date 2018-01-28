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
