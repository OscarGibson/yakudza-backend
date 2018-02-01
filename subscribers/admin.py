from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):

	class Meta:
		model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)