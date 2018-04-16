from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import CallBack

from django.conf import settings

from django.core.mail import send_mail

from django.template.loader import render_to_string


class CallBackViewSet(ViewSet):

	def post(self, request):

		name = request.data['name'] if 'name' in request.data else None
		phone = request.data['cell'] if 'cell' in request.data else None

		if not phone:
			return Response({'message':'Invalid data'}, status= 400)

		msg_html = render_to_string('callback/email.html', {'name': name, 'phone' : phone})

		is_sended = send_mail(
			'Вас просять передзвонити', 
			msg_html, 
			'admin@yakuzalviv.com', 
			['yakuzalviv@gmail.com', 'oneostap@gmail.com'], 
			html_message= msg_html,
			)

		CallBack(name= name, phone= phone).save()
		return Response({'message':'success'})
