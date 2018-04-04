from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from .models import Order
from product.models import Product, ProductManager, Add, AddManager
from rest_framework.response import Response

# from rest_framework.renderers import TemplateHTMLRenderer

from django.http import HttpResponse
from django.views.generic import View
# from .render_pdf import render_to_pdf
from django.template.loader import get_template


# from open_facebook.api import OpenFacebook

from django.conf import settings

from django.core.mail import send_mail

from django.template.loader import render_to_string

from liqpay.liqpay import LiqPay
from django.conf import settings

LIQPAY_PUBLIC_KEY = getattr(settings, 'LIQPAY_PUBLIC_KEY')
LIQPAY_PRIVATE_KEY = getattr(settings, 'LIQPAY_PRIVATE_KEY')

class OrderViewSet(ViewSet):

	def post(self, request):
		data = request.data

		if 'products' not in data:
			return Response({'message':'Invalid data'}, status= 400)

		products = data['products']
		total = 0
		try:
			order = Order.objects.create(
				address= data['address'],
				phone= data['phone'],
				name= data['name'],
				count= data['count'],
				comment= data['comment'] if 'comment' in data else None,
				total= total,
				is_payed= False,
				type_of_payment= 0
				)
		except Exception as e:
			print(e)
			return Response({'message':'Invalid data'}, status= 400)
		
		for product_data in products:
			product = get_object_or_404(Product, pk= product_data['pk'])
			product_manager = ProductManager(
				product= product,
				count= product_data['count']
				)
			product_manager.save()
			order.product.add(product_manager)
			total += product.price*product_data['count']

		order.total = total
		order.save()

		if 'type' in data and data['type'] == 1:
			print('PAyment by card')
			liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
			params = {
			    'action': 'pay',
			    'amount': total,
			    'currency': 'UAH',
			    'description': 'Yakuza food delivery',
			    'order_id': order.id,
			    'version': '3',
			    'sandbox' : 1,
			    'server_url': 'https://7e301535.ngrok.io/order/order-callback/',
			}

		signature = liqpay.cnb_signature(params)
		data = liqpay.cnb_data(params)

		return Response({
			'message' : 'redirect', 
			'data' : data, 
			'signature' : signature
		}, status= 200)

		msg_html = render_to_string('order/email.html', {'order': order, 'products' : products})
		msg_plain = render_to_string('order/email.txt', {'order': order, 'products' : products})

		is_sended = send_mail('Нове замовлення', msg_html, 'admin@yakuzalviv.com', ['yakuzalviv@gmail.com'], html_message=msg_html,)

		return Response({'message':'success'}, status= 201)


	def callback(self, request):

		# print('FACEBOOK_ACCESS_TOKEN ', access_token)

		# Getting info about me

		# Writing your first comment
		# is_set = facebook.set('me/comments', message= 'uhiuhi')

		# is_set = facebook.set('me/feed', message= [])
		# info_me = facebook.set('me/feed', message= 'lalka')

		# print('ME INFO ', info_me)

		# print('-'*12)
		# print(dir(facebook))

		return Response({
			'message':'success', 
			'content' : {
				# 'me_info' : info_me,
				# 'access_token' : access_token,
				# 'facebook dir' : dir(facebook)
				}
			})


# class OrderTemplateViewSet(View):

# 	def get(self, request, order_id):

# 		order = get_object_or_404(Order, pk= order_id)

# 		products = order.product.all()

# 		template = get_template('order/new_order.html')

# 		type_of_payment = 'Картка' if order.type_of_payment == 1 else 'Готівка'

# 		context = {
# 			'order' : order, 
# 			'products':products,
# 			'type_of_payment':type_of_payment
# 			}

# 		# html = template.render(context)
# 		# pdf = render_to_pdf('order/new_order.html', context)
# 		# if pdf:
# 		# 	response = HttpResponse(pdf, content_type='application/pdf')
# 		# 	filename = "Invoice_%s.pdf" %("12341231")
# 		# 	content = "inline; filename='%s'" %(filename)
# 		# 	download = request.GET.get("download")
# 		# 	if download:
# 		# 		content = "attachment; filename='%s'" %(filename)
# 		# 	response['Content-Disposition'] = content
# 		# 	return response
# 		# return HttpResponse("Not found")

# 		pdf = render_to_pdf('order/new_order.html', context)
# 		return HttpResponse(pdf, content_type='application/pdf')

"""
{
	"address" : "address",
	"phone" : 6546754,
	"comment" : "",
	"products" : [
	{"count":2, "pk":1}
	],
	"adds": []
}
"""




"""
curl -X POST -H "Content-Type: application/json" -d '{
  "messaging_type": "RESPONSE",
  "recipient": {
    "id": "2125950597692070"
  },
  "message": {
    "text": "hello, world!"
  }
}' "https://graph.facebook.com/v2.12/2125950597692070/messages?access_token=EAACEdEose0cBAGZBnlAN2ZBZCNEEDxASIg6bS5wZAh0VNYtictlvZAePcHzej3QZCzBraAqsFOzridx7yVlVpPM7WgaaCZARMjtOu0DYLalXmpHhfZB7P2ON5b09maGQVZACZCl0weyMsBZBEozP1hcfmZCoqcCq6VYqwV0P2saCnslTFRaGNyxltLo7J61CCGtDiKIa41Tu2lGqpQZDZD"
    
EAACEdEose0cBAGZBnlAN2ZBZCNEEDxASIg6bS5wZAh0VNYtictlvZAePcHzej3QZCzBraAqsFOzridx7yVlVpPM7WgaaCZARMjtOu0DYLalXmpHhfZB7P2ON5b09maGQVZACZCl0weyMsBZBEozP1hcfmZCoqcCq6VYqwV0P2saCnslTFRaGNyxltLo7J61CCGtDiKIa41Tu2lGqpQZDZD
"""






