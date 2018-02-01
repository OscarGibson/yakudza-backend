from django.contrib import admin
from .models import SharesSection, DocumentSection, HowToSection, ContactSection, \
						SocialSection, OrderSection, EmailSection


class SharesSectionAdmin(admin.ModelAdmin):
	class Meta:
		model = SharesSection

admin.site.register(SharesSection, SharesSectionAdmin)

class DocumentSectionAdmin(admin.ModelAdmin):
	class Meta:
		model = DocumentSection

admin.site.register(DocumentSection, DocumentSectionAdmin)

class HowToSectionAdmin(admin.ModelAdmin):
	class Meta:
		model = HowToSection

admin.site.register(HowToSection, HowToSectionAdmin)

class ContactSectionAdmin(admin.ModelAdmin):
	class Meta:
		model = ContactSection

admin.site.register(ContactSection, ContactSectionAdmin)

class SocialSectionAdmin(admin.ModelAdmin):
	class Meta:
		model = SocialSection

admin.site.register(SocialSection, SocialSectionAdmin)

class OrderSectionAdmin(admin.ModelAdmin):
	class Meta:
		model = OrderSection

admin.site.register(OrderSection, OrderSectionAdmin)

class EmailSectionAdmin(admin.ModelAdmin):
	class Meta:
		model = EmailSection

admin.site.register(EmailSection, EmailSectionAdmin)
