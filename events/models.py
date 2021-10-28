import string, secrets

from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings

alphabet = string.ascii_lowercase + string.digits


def randomCodeGen(length):
    return "".join(secrets.choice(alphabet) for x in range(length))

def passCodeGen(length=6):
    return ''.join(secrets.choice(alphabet + string.ascii_uppercase) for x in range(length))

def eventCodeGen(length=8):
    return randomCodeGen(length)

def ticketCodeGen(length=9):
    return randomCodeGen(length)

    

class Event(models.Model):
    code = models.CharField(primary_key=True, max_length = 50, default=eventCodeGen, editable=False, unique=True)
    title = models.CharField(max_length = 50)
    kind = models.CharField(max_length = 15)
    venue = models.CharField(max_length = 150)
    description = models.TextField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)

    max_guests = models.PositiveIntegerField(blank=True, null=True)
        
    account = models.PositiveIntegerField(blank=True, null=True)
    
    refundable = models.BooleanField(default=False)
    refund_deadline = models.DateTimeField(blank=True, null=True)
    

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.EmailField()
    pass_code = models.CharField(blank=True, max_length = 50, default=passCodeGen)

    
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title


class TicketClass(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="ticket_classes", blank=True, null=True)

    title = models.CharField(max_length = 50)
    description = models.TextField()

    cost = models.DecimalField(max_digits=9, decimal_places=2)

    
    class Meta:
        verbose_name = 'Ticket class'
        verbose_name_plural = 'Ticket classes'

    def __str__(self):
        return self.title


class RequestedInformation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="requested_Information", blank=True, null=True)

    title = models.CharField(max_length = 50)
    kind = models.CharField(max_length = 150, choices=settings.SUPPORTED_INPUT_TYPES)
    maxlength = models.IntegerField(blank=True, validators=[MaxValueValidator(200)])
    required = models.BooleanField(default=False)
    
    short_description = models.CharField(max_length = 50)
    description = models.TextField(blank=True)

    
    class Meta:
        verbose_name = 'requested information'
        verbose_name_plural = 'requested information'

    def __str__(self):
        return self.title


class RequestedInformationAnswer(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, related_name="requested_information_answers",  blank=True, null=True)
    requested_information = models.ForeignKey(RequestedInformation, on_delete=models.CASCADE, related_name="answers")
    answer = models.CharField(max_length = 150)

    class Meta:
        verbose_name = 'Extra info answer'
        verbose_name_plural = 'Extra info answers'

    def __str__(self):
        return f"{self.RequestedInformation.title} - {self.answer}"

class Ticket(models.Model):
    code = models.CharField(primary_key=True, max_length = 50, default=ticketCodeGen, editable=False, unique=True)

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    ticket_class = models.ForeignKey('TicketClass', on_delete=models.CASCADE, related_name="tickets")

    email = models.EmailField()


    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return f"ticket - {self.code}"
