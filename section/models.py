from django.db import models

class SharesSection(models.Model):
	""" Data for shares page """
	content = models.TextField()
	image = models.ImageField()
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	def __str__(self):
		if len(self.content) > 32:
			return "%s..." % self.content[:32]
		return self.content

class DocumentSection(models.Model):
	""" Data for document page """
	title = models.CharField(max_length= 64)
	content = models.TextField()
	image_1 = models.ImageField()
	image_2 = models.ImageField()
	image_3 = models.ImageField()
	image_4 = models.ImageField()
	image_5 = models.ImageField()
	image_6 = models.ImageField()
	created_at = models.DateTimeField(auto_now_add= True)
	updated_at = models.DateTimeField(auto_now= True)

	def __str__(self):
		if len(self.content) > 32:
			return self.content[:32]
		return self.content

class HowToSection(models.Model):
	""" Data for 'How To' page """
	title = models.CharField(max_length= 64)
	content = models.TextField()
	icon = models.ImageField()

	def __str__(self):
		if len(self.content) > 32:
			return self.content[:32]
		return self.content

class ContactSection(models.Model):
	""" Contacts numbers """
	ICONS_NAMES = (
		('kyivstar', 'kyivstar'),
		('vodafone', 'vodafone'),
		('lifecell', 'lifecell'),
		)
	icon = models.CharField(max_length= 32, choices= ICONS_NAMES)
	phone = models.IntegerField(default= 0)

	def __str__(self):
		return str(self.phone)

class EmailSection(models.Model):
	""" Contacts numbers """
	email = models.EmailField()

	def __str__(self):
		return str(self.email)

class SocialSection(models.Model):
	""" Social icons and links """

	ICONS_NAMES = (
		('facebook', 'facebook'),
		('vk', 'vk'),
		('twitter', 'twitter'),
		('google-plus', 'google-plus'),
		('instagram', 'instagram')
		)

	icon = models.CharField(max_length= 32, choices= ICONS_NAMES)
	link = models.CharField(max_length= 256)

	def __str__(self):
		print(self.icon)
		return self.icon

class OrderSection(models.Model):
	""" Content for order page """
	title = models.CharField(max_length= 64)
	related_categories = models.ManyToManyField("category.Category")

	def __str__(self):
		return self.title


class FooterSectionText(models.Model):
	""" Content for footer text """

	text = models.TextField()

	def __str__(self):
		return ("%s..." % self.text[:32]) if len(self.text) > 32 else self.text

class Votes(models.Model):
	""" Vote object """

	middle_mark = models.FloatField(default= 4.5)
	count = models.IntegerField(default= 17)

	def __str__(self):
		return "Оцінка %s, кількість голосів - %s" % (self.middle_mark, self.count)