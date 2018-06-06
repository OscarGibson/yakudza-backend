from django.db import models

class Product(models.Model):
	""" Model for product """
	title = models.CharField(max_length= 256)
	# slug = models.CharField(max_length= 256)
	description = models.TextField(blank= True)
	categories = models.ManyToManyField('category.Category')
	tags = models.ManyToManyField('tag.Tag', blank= True)
	image = models.ImageField()
	price = models.FloatField(default= 0)
	weight = models.IntegerField(default= 0)
	pieces = models.IntegerField(default= 0)
	label = models.ManyToManyField('Labels', blank= True)
	my_order = models.PositiveIntegerField(default= 0, blank= False, null= False)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	class Meta:
		verbose_name = "Продукт"
		verbose_name_plural = "Продукти"
		ordering = ['my_order']

	def __str__(self):
		return "%s: %sUAH" % (self.title, self.price)

class ProductManager(models.Model):
	""" Model for adding many products """
	product = models.ForeignKey('Product', on_delete= models.CASCADE)
	count = models.IntegerField()

	@property
	def total(self):
		return self.count * self.product.price

class Add(models.Model):
	""" Model for additional devices """
	name = models.CharField(max_length= 256)

	def __str__(self):
		return self.name

class AddManager(models.Model):
	""" Model for adding many adds """
	add = models.ForeignKey('Add', on_delete= models.PROTECT)
	count = models.IntegerField()


class Labels(models.Model):
	""" Labels for products """
	name = models.CharField(max_length= 64)
	icon = models.ImageField()

	def __str__(self):
		return self.name
