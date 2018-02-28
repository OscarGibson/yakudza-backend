from django.urls import path
from .views import OrderViewSet

urlpatterns = [
	path('', OrderViewSet.as_view({'post':'post','get':'test'}), name= 'Order'),
]