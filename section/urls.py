from django.urls import path
from .views import SharesViewSet, DocumentViewSet, HowToViewSet, \
					ContactViewSet, SocialViewSet, SectionViewSet, EmailViewSet

urlpatterns = [
    path('shares', SharesViewSet.as_view({'get':'get'}), name= 'Shares'),
    path('document', DocumentViewSet.as_view({'get':'get'}), name= 'document'),
    path('how-to', HowToViewSet.as_view({'get':'get'}), name= 'how to'),
    path('contact', ContactViewSet.as_view({'get':'get'}), name= 'Contacts'),
    path('email', EmailViewSet.as_view({'get':'get'}), name= 'Email'),
    path('social', SocialViewSet.as_view({'get':'get'}), name= 'Social'),
    path('menu', SectionViewSet.as_view({'get':'list'}), name= 'Menu'),
]