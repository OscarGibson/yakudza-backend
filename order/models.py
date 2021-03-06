from django.db import models
# from django.dispatch import receiver
# from django.db.models.signals import post_save
import uuid

def uuid_str():
    return str(uuid.uuid4())

class Order(models.Model):
	""" Model for order """

	PAYMENT_CHOICE = (
		('0', 'Готівка'),
		('1', 'Картка')
		)

	id = models.CharField(primary_key= True, default= uuid_str, editable= False, max_length= 64)
	simple_id = models.IntegerField(default= 0)
	product = models.ManyToManyField('product.ProductManager', blank= True)
	name = models.CharField(("Ім'я"), max_length= 256)
	count = models.IntegerField(("Кількість"),)
	address = models.CharField(("Адреса"), max_length= 256)
	phone = models.CharField(("Номер телефону"), max_length= 64)
	comment = models.TextField(("Коментарій"), blank= True)
	adds = models.ManyToManyField('product.AddManager', blank= True)
	type_of_payment = models.CharField(("Тип платежу"), max_length= 32,
										choices= PAYMENT_CHOICE,
										default= 0)
	is_payed = models.BooleanField(("Оплачено"), default= False)
	total = models.FloatField(("Всього"), blank= True)
	total_discount = models.FloatField(("Всього зі знижкою"), blank= True)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	def __str__(self):
		return "%s - %s" % (self.total, self.address)


# @receiver(post_save, sender= Order)
# def post_save_order(sender, instance, **kwargs):
#      product_managers = instance.product.all()
#      total = 0
#      for product_manager in product_managers:
#      	price = product_manager.product.price
#      	count = product_manager.count
#      	total += price*count
#      instance.total = total
#      instance.save()