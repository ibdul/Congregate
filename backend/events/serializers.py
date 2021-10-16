from rest_framework import serializers
from .models import Event, RequestedInformation,TicketClass

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
			# 'base_cost',
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

