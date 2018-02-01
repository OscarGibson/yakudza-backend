from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import SharesSection, DocumentSection, HowToSection, \
					ContactSection, SocialSection, OrderSection
from .serializers import SharesSectionSerializer, DocumentSectionSerializer,\
						HowToSectionSerializer, ContactSectionSerializer, \
						SocialSectionSerializer, OrderSectionSerializer


class SharesViewSet(ViewSet):

	def get(self, request):

		shares = SharesSection.objects.all()
		shares_out = SharesSectionSerializer(shares, many= True).data

		return Response({'shares_section':shares_out})

class DocumentViewSet(ViewSet):

	def get(self, request):

		document = DocumentSection.objects.all()
		document_out = DocumentSectionSerializer(document, many= True).data

		return Response({'document_section':document_out})

class HowToViewSet(ViewSet):

	def get(self, request):

		how_to = HowToSection.objects.all()
		how_to_out = HowToSectionSerializer(how_to, many= True).data

		return Response({'how_to_section':how_to_out})

class ContactViewSet(ViewSet):

	def get(self, request):

		contact = ContactSection.objects.all()
		contact_out = ContactSectionSerializer(contact, many= True).data

		return Response({'contact_section':contact_out})

class SocialViewSet(ViewSet):

	def get(self, request):

		social = SocialSection.objects.all()
		social_out = SocialSectionSerializer(social, many= True).data

		return Response({'social_section':social_out})

class OrderViewSet(ViewSet):

	def get(self, request):

		order = OrderSection.objects.all()
		order_out = OrderSectionSerializer(order, many= True).data

		return Response({'order_section':order_out})

class SectionViewSet(ViewSet):
	""" Get list of pages (menu) """
	def list(self, request):
		""" NOT FINISHED """
		return Response({
			'menu' : [
				{'title':'Shares', 'id':0},
				{'title':'Feedbacks', 'id':1},
				{'title':'Documents', 'id':2},
				{'title':'How to', 'id':3},
				{'title':'Constacts', 'id':4},
				# {'title':'Order', 'id':5}
			]
			})
			
