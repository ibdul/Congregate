import datetime
from urllib.parse import urlsplit

from django.core import validators as DjangoValidators
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime
from django.utils import formats as formatsFunc


from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .models import RequestedInformationAnswer, Event, RequestedInformation, TicketClass, Ticket
from .serializers import RequestedInformationAnswerSerializer, EventSerializer, RequestedInformationSerializer, TicketClassSerializer, TicketSerializer, FullTicketSerializer



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
        
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save()
            return Response({'success':"data valid", "ticket": ticket.code})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestedInformationAnswerViewSet(viewsets.ModelViewSet):
    queryset = RequestedInformationAnswer.objects.all()
    serializer_class = RequestedInformationAnswerSerializer
    permission_classes = [AllowAny]
    @action(detail=False, methods=['post'])
    def verify(self, request):
        serializer = self.get_serializer(data=request.data)
        requested_information = RequestedInformation.objects.filter(id=request.data['requested_information'])
        errors = []
        if serializer.is_valid():
            if requested_information.exists:
                requested_information = requested_information.first()
            else:
                # extra info question doesnt exist
                errors.append("question does not exist")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            #### answer validation
            answer = request.data['answer']
            answer = answer.strip()
            question_type = requested_information.kind
            if len(answer) == 0:
                if requested_information.required == True:
                    # answer required but not supplied
                    errors.append("answer required")

            else:
                validate = ""
                if question_type == 'email':
                    validate = DjangoValidators.EmailValidator()
                    try:
                        validate(answer)
                    except Exception as e:
                        errors.append(e)


                elif question_type == 'url':
                    """
                    Return a list of url parts via urlparse.urlsplit(), or raise
                    ValidationError for some malformed URLs.
                    """
                    try:
                        urlsplit(answer)
                    except Exception as e:
                        # urlparse.urlsplit can raise a ValueError with some
                        # misformatted URLs.
                        errors.append(e)
                        # raise ValidationError(self.error_messages['invalid'], code='invalid')
                else:
                    
                    #### TIME RELATED
                    def to_python(formats, value, stFunc):
                        # Try to strptime(stFunc) against each input format.
                        for format in formats:
                            try:
                                return stFunc(value, format)
                            except Exception as e:
                                return e

                    if question_type == 'time':
                        if not isinstance(answer, datetime.time):
                            formats = formatsFunc.get_format_lazy('TIME_INPUT_FORMATS')
                        def strptime(self, value, format):
                            return datetime.datetime.strptime(value, format).time()
                        if not to_python(formats, answer,  strptime):
                                errors.append(f"not a valid time {e}")

                    elif question_type == 'date':
                        if not isinstance(answer, datetime.date):
                            formats = formatsFunc.get_format_lazy('DATE_INPUT_FORMATS')
                            def strptime(self, value, format):
                                return datetime.datetime.strptime(value, format).date()
                            if not to_python(formats, answer,  strptime):
                                errors.append(f"not a valid date {e}")

                    elif question_type == 'datetime-local':
                        def __iter__(self):
                            yield from formatsFunc.get_format('DATETIME_INPUT_FORMATS')
                            yield from formatsFunc.get_format('DATE_INPUT_FORMATS')

                        if not isinstance(answer, datetime.datetime):
                            formats = DateTimeFormatsIterator()
                            if isinstance(answer, datetime.date):
                                errors.append('Time not provided')
                            else:
                                try:
                                    result = parse_datetime()
                                except Exception as e:
                                    errors.append(f"not a valid date {e}")
                                if not result:
                                    def strptime(self, value, format):
                                        return datetime.datetime.strptime(value, format)
                                    if not to_python(formats, answer,  strptime):
                                        errors.append(f"not a valid date {e}")

                    elif question_type == 'number':
                        if not answer.isnumeric():
                            errors.append('number required')

            
            if len(errors) == 0:
                return Response({'success': "answer data valid"})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupportedDataTypes(APIView):
    def get(self, request, format=None):
        return Response(settings.SUPPORTED_INPUT_TYPES)

class Statistics(APIView):
    def get(self, request, format=None):
        events = Event.objects.all().count()
        tickets = Ticket.objects.all().count()
        return Response({'tickets':tickets, "events": events})

