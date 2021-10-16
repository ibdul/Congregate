from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Event, RequestedInformation, TicketClass
from .serializers import  EventSerializer, RequestedInformationSerializer, TicketClassSerializer



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, pk=None):
        event = get_object_or_404(self.queryset, code=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def fetch(self, request, pk=None):
        event = get_object_or_404(self.queryset, code=pk)
        serializer = EventSerializer(event)
        ticket_classes = TicketClassSerializer(TicketClass.objects.filter(event=event), many=True)
        requested_information = RequestedInformationSerializer(RequestedInformation.objects.filter(event=event), many=True)

        return Response({
            "event": serializer.data,
            "requested_information" : requested_information.data,
            "ticket_classes": ticket_classes.data
            })



    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            return Response({'success':"data valid", "event": event.code, 'pass': event.pass_code})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestedInformationViewSet(viewsets.ModelViewSet):
    queryset = RequestedInformation.objects.all()
    serializer_class = RequestedInformationSerializer
    permission_classes = [AllowAny]


    @action(detail=False, methods=['post'])
    def verify(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({'success':"data valid"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TicketClassViewSet(viewsets.ModelViewSet):
    queryset = TicketClass.objects.all()
    serializer_class = TicketClassSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def verify(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response({'success':"data valid"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SupportedDataTypes(APIView):
    def get(self, request, format=None):
        return Response(settings.SUPPORTED_INPUT_TYPES)

class Statistics(APIView):
    def get(self, request, format=None):
        events = Event.objects.all().count()
        tickets = 123
        # tickets = Ticket.objects.all().count()
        return Response({'tickets':tickets, "events": events})

