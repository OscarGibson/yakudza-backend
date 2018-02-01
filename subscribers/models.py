from django.db import models

class Subscriber(models.Model):
	""" Create subscriber for email sending """

	email = models.EmailField(max_length= 256)

	def __str__(self):
		return self.email