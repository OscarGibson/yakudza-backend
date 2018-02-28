from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from .models import Order
from product.models import Product, ProductManager, Add, AddManager
from rest_framework.response import Response

class OrderViewSet(ViewSet):

	def post(self, request):
		data = request.data

		print(data)

		if 'products' not in data:
			return Response({'message':'Invalid data'}, status= 400)

		products = data['products']
		adds = []#data['adds'] No need any more
		total = 0
		try:
			order = Order.objects.create(
				address= data['address'],
				phone= data['phone'],
				comment= data['comment'] if 'comment' in data else None,
				total= total,
				is_payed= False,
				type_of_payment= 0
				)
		except Exception as e:
			return Response({'message':'Invalid data'}, status= 400)
		# order.save()
		
		for product_data in products:
			product = get_object_or_404(Product, pk= product_data['pk'])
			product_manager = ProductManager(
				product= product,
				count= product_data['count']
				)
			product_manager.save()
			order.product.add(product_manager)
			total += product.price*product_data['count']

		for add_data in adds:
			add = get_object_or_404(Add, pk= add_data['pk'])
			add_manager = AddManager(
				product= add,
				count= add_data['count']
				)
			product_manager.save()
			order.adds.add(add_manager)

		order.total = total
		order.save()
		return Response({'message':'success'}, status= 201)

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