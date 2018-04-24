from django.shortcuts import render
from category.models import Category
from product.models import Product
from section.models import SharesSection
import json
from urllib.parse import parse_qs
from order.models import Order
from django.shortcuts import get_object_or_404
from product.models import Product, ProductManager

from django.conf import settings

from django.core.mail import send_mail

from django.template.loader import render_to_string

from liqpay.liqpay3 import LiqPay

from subscribers.models import Subscriber
# from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from section.models import SocialSection
from callback.models import CallBack
from feedback.models import Feedback

from django.db.models import Q

LIQPAY_PUBLIC_KEY = getattr(settings, 'LIQPAY_PUBLIC_KEY')
LIQPAY_PRIVATE_KEY = getattr(settings, 'LIQPAY_PRIVATE_KEY')

def main_page(request):

	categoires = Category.objects.all()

	socials = SocialSection.objects.all()

	search_key = request.GET.get('search', '')

	output = []

	args = (
		Q(title__contains= search_key) |
		Q(description__contains= search_key)
	)

	for category in categoires:
		products = Product.objects.filter(Q(categories= category) & args)
		output.append({
					'name' : category.name,
					'slug' : category.slug,
					'is_show' : category.is_show,
					'products' : products
					}
		)

	shares = SharesSection.objects.all()

	content = {
		'output' : output,
		'shares' : shares,
		'socials' : socials
	}

	template = 'page/main.html'

	return render(request, template, content)

def success(request):

	socials = SocialSection.objects.all()

	output = []

	categoires = Category.objects.all()


	for category in categoires:
		products = Product.objects.filter(categories= category)
		output.append({
					'name' : category.name,
					'slug' : category.slug,
					'is_show' : category.is_show,
					}
		)

	shares = SharesSection.objects.all()

	content = {
		'output' : output,
		'shares' : shares,
		'socials' : socials,
	}

	template = 'page/success.html'

	return render(request, template, content)

def success_callback(request):

	socials = SocialSection.objects.all()

	output = []

	categoires = Category.objects.all()


	for category in categoires:
		products = Product.objects.filter(categories= category)
		output.append({
					'name' : category.name,
					'slug' : category.slug,
					'is_show' : category.is_show,
					}
		)

	shares = SharesSection.objects.all()

	content = {
		'output' : output,
		'shares' : shares,
		'socials' : socials,
	}

	template = 'page/success_callback.html'

	return render(request, template, content)

def shares(request):

	socials = SocialSection.objects.all()

	shares = SharesSection.objects.all()

	output = []

	categoires = Category.objects.all()


	for category in categoires:
		products = Product.objects.filter(categories= category)
		output.append({
					'name' : category.name,
					'slug' : category.slug,
					'is_show' : category.is_show,
					}
		)

	content = {
		'shares' : shares,
		'socials' : socials,
		'output' : output
	}
	template = 'page/shares.html'

	return render(request, template, content)

def feedback(request):
	if request.method == 'POST':

		data = parse_qs(request.POST.get('request'))

		print('data', data['name'], data['comment'])

		author = data['name'][0] if 'name' in data else None
		phone = data['cell'][0] if 'cell' in data else None
		content = data['comment'][0] if 'comment' in data else None

		if not (author and content):
			return JsonResponse({'message':'Invalid data'}, status= 400)

		Feedback(author= author, phone= phone, content= content).save()

		return JsonResponse({'message':'Success'})
	elif request.method == 'GET':

		feedbacks = Feedback.objects.all()

		socials = SocialSection.objects.all()

		output = []

		categoires = Category.objects.all()


		for category in categoires:
			products = Product.objects.filter(categories= category)
			output.append({
						'name' : category.name,
						'slug' : category.slug,
						'is_show' : category.is_show,
						}
			)

		shares = SharesSection.objects.all()

		content = {
			'output' : output,
			'shares' : shares,
			'socials' : socials,
			'feedbacks' : feedbacks
		}

		tempalte = 'page/feedback.html'

		return render(request, tempalte, content)

def documents(request): pass

def how_to(request):
	categoires = Category.objects.all()

	socials = SocialSection.objects.all()

	output = []

	for category in categoires:
		products = Product.objects.filter(categories= category)
		output.append({
					'name' : category.name,
					'slug' : category.slug,
					'products' : products
					}
		)

	shares = SharesSection.objects.all()

	content = {
		'output' : output,
		'shares' : shares,
		'socials' : socials
	}
	template = 'page/howto.html'

	return render(request, template, content)

def contacts(request):

	socials = SocialSection.objects.all()

	output = []

	categoires = Category.objects.all()


	for category in categoires:
		products = Product.objects.filter(categories= category)
		output.append({
					'name' : category.name,
					'slug' : category.slug,
					'is_show' : category.is_show,
					}
		)

	content = {
		'socials' : socials,
		'output' : output
	}
	template = 'page/contacts.html'

	return render(request, template, content)

def checkout(request, post_data= None):

	if request.method == "POST":

		json_data = request.POST.get('data')
		data = json.loads(json_data)

		products = data['items']
		form = parse_qs(data['form'])
		# type_of_payment = data['type']

		total = 0
		total_discount = 0

		try:
			order = Order.objects.create(
				simple_id= len(Order.objects.all()),
				address= form['address'][0],
				phone= form['number'][0],
				name= form['name'][0],
				count= form['count'][0],
				comment= form['comment'][0] if 'comment' in data else "",
				total= total,
				total_discount= total_discount,
				is_payed= False,
				type_of_payment= 0
				)
		except Exception as e:
			print(e)
			# raise e
			return JsonResponse({'message':'Invalid data'}, status= 400)

		product_managers = []

		for product_data in products:
			product = get_object_or_404(Product, pk= product_data['item_id'])
			product_manager = ProductManager(
				product= product,
				count= product_data['quantity']
				)
			product_managers.append(product_manager)
			product_manager.save()
			order.product.add(product_manager)
			total += product.price*product_data['quantity']

		order.total = total
		order.total_discount = total

		if 'email' in data and data['email']:
			subscribers = Subscriber.objects.filter(email= data['email'])
			if len(subscribers) > 0 and subscribers[0].used_promotion == False:
				total_discount = total * 0.9
				order.total_discount = total_discount
				subscribers[0].used_promotion = True
				subscribers[0].save()

		order.save()

		if 'type' in data and data['type'] == 1:
			print('Payment by card', order.id)
			liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
			params = {
			    'action': 'pay',
			    'amount': total,
			    'currency': 'UAH',
			    'description': 'Yakuza food delivery',
			    'order_id': str(order.id),
			    'version': '3',
			    'sandbox' : 0,
			    'server_url': 'http://www.yakuzalviv.com/backend/api/v1/order/order-callback/',
			}

			signature = liqpay.cnb_signature(params)
			hash_data = liqpay.cnb_data(params)

			return JsonResponse({
				'message' : 'redirect',
				'order_id' : str(order.id),
				'signature' : signature,
				'hash_data' : hash_data,
			}, status= 200)

		msg_html = render_to_string('order/email.html', {'order': order, 'products' : product_managers})
		msg_plain = render_to_string('order/email.txt', {'order': order, 'products' : products})

		is_sended = send_mail('Нове замовлення', msg_html, 'admin@yakuzalviv.com', ['yakuzalviv@gmail.com', 'oneostap@gmail.com'], html_message=msg_html,)


		template = 'page/success.html'

		return JsonResponse({'message':'Success'}, status= 200)

	elif request.method == "GET":

		socials = SocialSection.objects.all()

		categoires = Category.objects.all()

		output = []

		for category in categoires:
			products = Product.objects.filter(categories= category)
			output.append({
						'name' : category.name,
						'slug' : category.slug,
						'products' : products
						}
			)

		shares = SharesSection.objects.all()

		content = {
			'output' : output,
			'shares' : shares,
			'socials' : socials
		}

		template = 'page/checkout.html'

		return render(request, template, content)

def callback(request):

	if request.method == "POST":

		data = parse_qs(request.POST.get('data'))

		print(data)

		name = data['name'] if 'name' in data else " "
		phone = data['number'] if 'number' in data else None

		if not phone:
			return JsonResponse({'message':'Invalid data'}, status= 400)

		msg_html = render_to_string('callback/email.html', {'name': name, 'phone' : phone})

		is_sended = send_mail(
			'Вас просять передзвонити',
			msg_html,
			'admin@yakuzalviv.com',
			['yakuzalviv@gmail.com', 'oneostap@gmail.com'],
			html_message= msg_html,
			)

		CallBack(name= name, phone= phone).save()
		return JsonResponse({'message':'Success'})

	return JsonResponse({}, status= 403)






