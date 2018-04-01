from django.shortcuts import render
from category.models import Category
from product.models import Product
from section.models import SharesSection
# import json

def main_page(request):

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
	}

	template = 'page/main.html'

	return render(request, template, content)

def shares(request):

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
	}
	template = 'page/shares.html'

	return render(request, template, content)

def feedback(request): pass

def documents(reqeust): pass

def how_to(reqeust): pass

def contacts(reqeust): pass

def checkout(request, post_data= None):

	content = {
		# 'output' : output,
	}
	template = 'page/checkout.html'

	return render(request, template, content)

