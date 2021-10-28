from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import SupportedDataTypes, RequestedInformationAnswerViewSet, EventViewSet, RequestedInformationViewSet, TicketClassViewSet, TicketViewSet, Statistics

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('requested-info', RequestedInformationViewSet)
router.register('ticket-classes', TicketClassViewSet)
router.register('requested-information-answers', RequestedInformationAnswerViewSet)
router.register('tickets', TicketViewSet)



urlpatterns = [
    path('get-data-types/', SupportedDataTypes.as_view()),
    path('', include(router.urls)),
    path('statistics/', Statistics.as_view()),
]