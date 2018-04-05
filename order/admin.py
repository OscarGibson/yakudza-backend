from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):

	list_display = ('address', 'total', 'is_payed', 'type_of_payment')
	fields = ('address', 'count', 'total', 'is_payed', 'type_of_payment', 'address', 'phone', 'comment')

	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)
