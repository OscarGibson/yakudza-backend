from django.urls import path
from .views import SharesViewSet, DocumentViewSet, HowToViewSet, \
					ContactViewSet, SocialViewSet, SectionViewSet, \
					OrderViewSet, EmailViewSet, FooterViewSet

urlpatterns = [
    path('shares', SharesViewSet.as_view({'get':'get'}), name= 'Shares'),
    path('document', DocumentViewSet.as_view({'get':'get'}), name= 'document'),
    path('how-to', HowToViewSet.as_view({'get':'get'}), name= 'how to'),
    path('contact', ContactViewSet.as_view({'get':'get'}), name= 'Contacts'),
    path('email', EmailViewSet.as_view({'get':'get'}), name= 'Email'),
    path('social', SocialViewSet.as_view({'get':'get'}), name= 'Social'),
    path('order', OrderViewSet.as_view({'get':'get'}), name= 'Order'),
    path('menu', SectionViewSet.as_view({'get':'list'}), name= 'Menu'),
    path('footer', FooterViewSet.as_view({'get':'get','post':'post'}), name= "Footer")
]