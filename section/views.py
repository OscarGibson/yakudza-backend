from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import SharesSection, DocumentSection, HowToSection, \
					ContactSection, SocialSection, OrderSection, EmailSection,\
					FooterSectionText, Votes
from .serializers import SharesSectionSerializer, DocumentSectionSerializer,\
						HowToSectionSerializer, ContactSectionSerializer, \
						SocialSectionSerializer, OrderSectionSerializer, \
						EmailSectionSerializer


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

class EmailViewSet(ViewSet):

	def get(self, request):

		email = EmailSection.objects.all()
		email_out = EmailSectionSerializer(email, many= True).data

		return Response({'email_section':email_out})

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
				{'title':'Акції', 'id':0},
				{'title':'Відгуки', 'id':1},
				# {'title':'Документи', 'id':2},
				{'title':'Як замовити', 'id':3},
				{'title':'Контакти', 'id':4}
			]
			})

class FooterViewSet(ViewSet):
	""" Get footer text and votes, post votes """

	def get(self, request):
		votes = {'mark' : 4.5, 'count' : 17}
		footer_text = []
		try:
			footer_text = FooterSectionText.objects.all()[0].text
		except Exception as e:
			pass
		try:
			vote = Votes.objects.all()[0]
			votes['mark'] = vote.middle_mark
			votes['count'] = vote.count
		except Exception as e:
			pass

		return Response({'text':footer_text, 'votes':votes})

	def post(self, request):

		try:
			vote = Votes.objects.all()[0]
			vote.count += 1
			vote.save()
		except Exception as e:
			return Response({'message':'Server error', 'error': e.message}, status= 500)
		return Response({'message':'success'})