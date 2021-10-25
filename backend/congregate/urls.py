from django.contrib import admin
from django.urls import path, include
from django.conf import settings

adminAddress = settings.ADMIN_ADDRESS
urlpatterns = [
    path(f'{adminAddress}/', admin.site.urls),
    path('api/v1/feedback/', include('feedback.urls')),
    path('api/v1/', include('events.urls')),
]
