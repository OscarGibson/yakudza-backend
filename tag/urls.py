from django.urls import path
from .views import TagViewSet

urlpatterns = [
    path('', TagViewSet.as_view({'get':'get'}), name= 'Tag'),
]