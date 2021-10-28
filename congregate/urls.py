from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from django.views.generic import TemplateView


adminAddress = settings.ADMIN_ADDRESS
urlpatterns = [
    path(f'{adminAddress}/', admin.site.urls),


    #API RELATED

    path('api/v1/feedback/', include('feedback.urls')),
    path('api/v1/', include('events.urls')),

    
    path('', TemplateView.as_view(template_name="index.html")),
]
