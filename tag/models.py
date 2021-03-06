from django.db import models

class Tag(models.Model):
	""" Model for tag """
	name = models.CharField(max_length= 256)
	slug = models.CharField(max_length= 256)
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	def __str__(self):
		return self.name
