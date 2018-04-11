from django.db import models

class Subscriber(models.Model):
	""" Create subscriber for email sending """

	email = models.EmailField("Емейл", max_length= 256)
	used_promotion = models.BooleanField("Знижка використана", default= False)

	def __str__(self):
		return self.email