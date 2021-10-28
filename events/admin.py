from django.contrib import admin

from .models import Event, RequestedInformation, RequestedInformationAnswer, TicketClass, Ticket

admin.site.register(Event)
admin.site.register(RequestedInformation)
admin.site.register(TicketClass)
admin.site.register(Ticket)
admin.site.register(RequestedInformationAnswer)