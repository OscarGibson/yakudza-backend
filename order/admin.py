from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):

	fields = ('address', 'total', 'is_payed', 'type_of_payment')

	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)
