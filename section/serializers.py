from rest_framework.serializers import ModelSerializer
from .models import SharesSection, DocumentSection, HowToSection, ContactSection, \
						SocialSection, OrderSection, EmailSection


class SharesSectionSerializer(ModelSerializer):
	""" Shares serializer """
	class Meta:
		model = SharesSection
		fields = '__all__'

class DocumentSectionSerializer(ModelSerializer):
	""" Document serializer """
	class Meta:
		model = DocumentSection
		fields = '__all__'

class HowToSectionSerializer(ModelSerializer):
	""" HowTo serializer """
	class Meta:
		model = HowToSection
		fields = '__all__'

class ContactSectionSerializer(ModelSerializer):
	""" Contact serializer """
	class Meta:
		model = ContactSection
		fields = '__all__'

class EmailSectionSerializer(ModelSerializer):
	""" Email serializer """
	class Meta:
		model = EmailSection
		fields = '__all__'

class SocialSectionSerializer(ModelSerializer):
	""" Social serializer """
	class Meta:
		model = SocialSection
		fields = '__all__'

class OrderSectionSerializer(ModelSerializer):
	""" Order serializer """
	class Meta:
		model = OrderSection
		fields = '__all__'