from django.contrib import admin
from .models import Category
from adminsortable2.admin import SortableAdminMixin

class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
	class Meta(object):
		model = Category

admin.site.register(Category, CategoryAdmin)
