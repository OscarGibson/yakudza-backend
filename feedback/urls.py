from django.urls import path
from .views import FeedbackViewSet

urlpatterns = [
    path('', FeedbackViewSet.as_view({'get':'get'}), name= 'Feedback'),
]