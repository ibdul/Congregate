from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import SupportedDataTypes,  EventViewSet, RequestedInformationViewSet, TicketClassViewSet,  Statistics

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('requested-info', RequestedInformationViewSet)
router.register('ticket-classes', TicketClassViewSet)


urlpatterns = [
    path('get-data-types/', SupportedDataTypes.as_view()),
    path('', include(router.urls)),
    path('statistics/', Statistics.as_view()),
]