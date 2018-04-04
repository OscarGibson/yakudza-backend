from django.urls import path
from .views import OrderViewSet
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	path('', csrf_exempt(OrderViewSet.as_view({'post':'post'})), name= 'Order'),
	path('order-callback/', csrf_exempt(OrderViewSet.as_view({'post' : 'callback'})), name= 'Order callback'),
	path('test/', OrderViewSet.as_view({'get':'get'}), name= 'Order Template')
]