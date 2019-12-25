from django.db import models

class Category(models.Model):
	""" Model for category """
	name = models.CharField(max_length= 128, unique= True)
	slug = models.CharField(max_length= 128)
	is_show = models.BooleanField("Відображати", default= True)
	my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	def __str__(self):
		return self.name

	class Meta(object):
	    ordering = ['my_order']