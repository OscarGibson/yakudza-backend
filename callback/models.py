from django.db import models

class CallBack(models.Model):
	""" Create model with phone number for callback """

	phone = models.CharField(max_length= 12)
	name  = models.CharField(max_length= 64)

	def __str__(self):
		return "%s : %s" % (self.name, self.phone)
