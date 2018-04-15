"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

api_path = 'backend/api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('%sproduct' % api_path, include('product.urls')),
    path('%scategory' % api_path, include('category.urls')),
    path('%stag' % api_path, include('tag.urls')),
    path('%ssection/' % api_path, include('section.urls')),
    path('%sfeedback' % api_path, include('feedback.urls')),
    path('%ssubs' % api_path, include('subscribers.urls')),
    path('%scallback' % api_path, include('callback.urls')),
    path('%sorder/' % api_path, include('order.urls')),
    path('pages/', include('page.urls'))

    # path('facebook/', include('django_facebook.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
