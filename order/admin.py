from django.contrib import admin
from .models import Order

def type_of_payment_str(obj):
    return ("%s" % ("Картка" if obj.type_of_payment == 1 else "Готівка")).upper()
type_of_payment_str.short_description = 'Тип оплати'

class OrderAdmin(admin.ModelAdmin):

	list_display = ('address', 'total', 'is_payed', 'type_of_payment_str')
	fields = ('address', 'count', 'total', 'is_payed', 'type_of_payment', 'address', 'phone', 'comment')

	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)
