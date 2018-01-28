from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	class Meta:
		model = Feedback

admin.site.register(Feedback, FeedbackAdmin)
