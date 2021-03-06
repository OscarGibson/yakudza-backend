from django.db import models

class Feedback(models.Model):

	author = models.CharField(max_length= 256)
	phone = models.CharField(max_length= 12, blank= True)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	def __str__(self):
		if len(self.content) > 32:
			return "%s: %s..." % (self.author, self.content[:32])
		return "%s: %s" % (self.author, self.content)

	class Meta:
		ordering = ('-created_at',)