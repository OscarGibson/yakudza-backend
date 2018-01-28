from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category

admin.site.register(Category, CategoryAdmin)
