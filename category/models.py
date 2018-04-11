from django.db import models

class Category(models.Model):
	""" Model for category """
	name = models.CharField(max_length= 256, unique= True)
	slug = models.CharField(max_length= 256)
	is_show = models.BooleanField("Відображати", default= True)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	def __str__(self):
		return self.name
