from django.urls import path
from .views import OrderViewSet

urlpatterns = [
	path('', OrderViewSet.as_view({'post':'post'}), name= 'Order'),
	path('order-callback/', OrderViewSet.as_view({'post' : 'callback'}), name= 'Order callback'),
	path('test/', OrderViewSet.as_view({'get':'get'}), name= 'Order Template')
]