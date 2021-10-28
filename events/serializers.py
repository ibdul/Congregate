from rest_framework import serializers
from .models import RequestedInformationAnswer, Event, RequestedInformation,TicketClass, Ticket

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = [
			'code',
			'title',
			'kind',
			'venue',
			'description',
			'start_date',
			'end_date',
			'max_guests',
			'account',
			'refundable',
			'refund_deadline',
			'created_by',
		]

class RequestedInformationSerializer(serializers.ModelSerializer):
	class Meta:
		model=RequestedInformation
		fields=('id', "event", 'title', 'kind', 'maxlength', 'required', 'short_description', 'description', )

class TicketClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = TicketClass
		fields = ('id', "event", 'title', 'description', 'cost',)

class RequestedInformationAnswerSerializer(serializers.ModelSerializer):

	class Meta:
		model = RequestedInformationAnswer
		fields = ('id', 'ticket', 'requested_information', 'answer')

class RequestedInformationAnswerSerializerX(serializers.ModelSerializer):
	requested_information = serializers.SlugRelatedField(read_only= True, slug_field="title")

	class Meta:
		model = RequestedInformationAnswer
		fields = ('id', 'ticket', 'requested_information', 'answer')

		
class TicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ticket
		fields = ('code', 'event', 'ticket_class', 'email', )


class FullTicketSerializer(serializers.ModelSerializer):
	ticket_class = serializers.SlugRelatedField(read_only= True, slug_field="title")
	requested_information_answers = RequestedInformationAnswerSerializerX(many=True, read_only=True)

	class Meta:
		model = Ticket
		fields = ('code', 'event', 'ticket_class', 'email', 'requested_information_answers', )