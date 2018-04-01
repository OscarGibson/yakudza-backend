from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name= 'Main'),
    path('shares', views.shares, name= 'Shares'),
    path('feedback', views.feedback, name= 'Feedback'),
    path('how-to', views.how_to, name= 'How to'),
    path('contacts', views.contacts, name= 'Contacts'),
    path('checkout', views.checkout, name= 'Checkout'),
]