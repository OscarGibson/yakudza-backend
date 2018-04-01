from django.contrib import admin
from .models import Product, Add, ProductManager, AddManager, Labels

class ProductAdmin(admin.ModelAdmin):
	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)

class AddAdmin(admin.ModelAdmin):
	class Meta:
		model = Add

admin.site.register(Add, AddAdmin)

class ProductManagerAdmin(admin.ModelAdmin):
	class Meta:
		model = ProductManager

# admin.site.register(ProductManager, ProductManagerAdmin)

class AddManagerAdmin(admin.ModelAdmin):
	class Meta:
		model = AddManager

# admin.site.register(AddManager, AddManagerAdmin)

class LabelAdmin(admin.ModelAdmin):
	class Meta:
		model = Labels

admin.site.register(Labels, LabelAdmin)
