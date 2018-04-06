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

from liqpay.liqpay3 import LiqPay
from django.conf import settings

LIQPAY_PUBLIC_KEY = getattr(settings, 'LIQPAY_PUBLIC_KEY')
LIQPAY_PRIVATE_KEY = getattr(settings, 'LIQPAY_PRIVATE_KEY')

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
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
				type_of_payment= data['type']
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
			print('Payment by card', order.id)
			liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
			params = {
			    'action': 'pay',
			    'amount': total,
			    'currency': 'UAH',
			    'description': 'Yakuza food delivery',
			    'order_id': order.id,
			    'version': '3',
			    'sandbox' : 1,
			    'server_url': 'http://www.yakuzalviv.com/backend/api/v1/order/order-callback/',
			}

		signature = liqpay.cnb_signature(params)
		hash_data = liqpay.cnb_data(params)

		return Response({
			'message' : 'redirect', 
			'order_id' : order.id, 
			'signature' : signature,
			'hash_data' : hash_data,
		}, status= 200)

		msg_html = render_to_string('order/email.html', {'order': order, 'products' : products})
		msg_plain = render_to_string('order/email.txt', {'order': order, 'products' : products})

		is_sended = send_mail('Нове замовлення', msg_html, 'admin@yakuzalviv.com', ['yakuzalviv@gmail.com', 'oneostap@gmail.com'], html_message=msg_html,)

		return Response({'message':'success'}, status= 201)


	def callback(self, request):

		print('CALL_BACK ', request.data)

		liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
		signature = request.data['signature']
		data = request.data['data']
		sign = liqpay.str_to_sign(LIQPAY_PRIVATE_KEY + data + LIQPAY_PRIVATE_KEY)
		if sign != signature:
			return Response({
				'message':'error', 
				'content' : {}
				}, status= 403)

		response = liqpay.decode_data_from_str(data)
		# print('callback data', response)

		try:
			order = Order.objects.get(id= response['order_id'])
			order.is_payed = True
			order.save()

			msg_html = render_to_string('order/email.html', {'order': order, 'products' : products})
			msg_plain = render_to_string('order/email.txt', {'order': order, 'products' : products})

			is_sended = send_mail('Нове замовлення', msg_html, 'admin@yakuzalviv.com', ['yakuzalviv@gmail.com', 'oneostap@gmail.com'], html_message=msg_html,)
			# send email
			return Response({
				'message':'success', 
				'content' : {}
				})
		except Exception as e:
			return Response({
					'message':'order not found', 
					'content' : {}
					}, status= 404)


	def get(self, request):
		d = {'signature': ['5mGjy2dCYxPIkmp66u1EsAhCUFY='], 'data': ['eyJhY3Rpb24iOiJwYXkiLCJwYXltZW50X2lkIjo2NjY2MTM3OTcsInN0YXR1cyI6InNhbmRib3giLCJ2ZXJzaW9uIjozLCJ0eXBlIjoiYnV5IiwicGF5dHlwZSI6ImNhcmQiLCJwdWJsaWNfa2V5IjoiaTUyMDMxNDY0MjIwIiwiYWNxX2lkIjo0MTQ5NjMsIm9yZGVyX2lkIjoiMjkiLCJsaXFwYXlfb3JkZXJfaWQiOiJIWTdCRFVRMDE1MjI4Njg2ODEzMTI0NTkiLCJkZXNjcmlwdGlvbiI6Illha3V6YSBmb29kIGRlbGl2ZXJ5Iiwic2VuZGVyX2NhcmRfbWFzazIiOiI0MTQ5NDkqOTciLCJzZW5kZXJfY2FyZF9iYW5rIjoicGIiLCJzZW5kZXJfY2FyZF90eXBlIjoidmlzYSIsInNlbmRlcl9jYXJkX2NvdW50cnkiOjgwNCwiaXAiOiI5MS4yMjUuMjAxLjY5IiwiYW1vdW50IjoxLjAsImN1cnJlbmN5IjoiVUFIIiwic2VuZGVyX2NvbW1pc3Npb24iOjAuMCwicmVjZWl2ZXJfY29tbWlzc2lvbiI6MC4wMywiYWdlbnRfY29tbWlzc2lvbiI6MC4wLCJhbW91bnRfZGViaXQiOjEuMCwiYW1vdW50X2NyZWRpdCI6MS4wLCJjb21taXNzaW9uX2RlYml0IjowLjAsImNvbW1pc3Npb25fY3JlZGl0IjowLjAzLCJjdXJyZW5jeV9kZWJpdCI6IlVBSCIsImN1cnJlbmN5X2NyZWRpdCI6IlVBSCIsInNlbmRlcl9ib251cyI6MC4wLCJhbW91bnRfYm9udXMiOjAuMCwibXBpX2VjaSI6IjciLCJpc18zZHMiOmZhbHNlLCJjcmVhdGVfZGF0ZSI6MTUyMjg2ODY4MTM1MCwiZW5kX2RhdGUiOjE1MjI4Njg2ODEzNTAsInRyYW5zYWN0aW9uX2lkIjo2NjY2MTM3OTd9']}

		return Response({
			'message':'success', 
			'content' : d
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






