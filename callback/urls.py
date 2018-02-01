from django.urls import path
from .views import CallBackViewSet

urlpatterns = [
    path('', CallBackViewSet.as_view({'post':'post'}), name= 'Callback'),
]