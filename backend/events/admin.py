from django.contrib import admin

from .models import Event, RequestedInformation, TicketClass

admin.site.register(Event)
admin.site.register(RequestedInformation)
admin.site.register(TicketClass)