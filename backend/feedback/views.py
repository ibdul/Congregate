from .models import Message
from .serializers import MessageSerializer

from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]