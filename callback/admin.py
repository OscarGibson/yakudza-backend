from django.contrib import admin
from .models import CallBack

class CallBackAdmin(admin.ModelAdmin):

	class Meta:
		model = CallBack

admin.site.register(CallBack, CallBackAdmin)
