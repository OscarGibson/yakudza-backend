from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

	list_display = ('address', 'total', 'is_payed', 'type_of_payment_str', 'created_at')
	fields = ('address', 'count', 'total', 'is_payed', 'type_of_payment', 'phone', 'comment')
	readonly_fields = ('created_at',)
	ordering = ('-created_at',)

	class Meta:
		model = Order

	def type_of_payment_str(self, obj):
		return "Картка" if obj.type_of_payment == "1" else "Готівка"
	type_of_payment_str.short_description = 'Тип оплати'

admin.site.register(Order, OrderAdmin)
