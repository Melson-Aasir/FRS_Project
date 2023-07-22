from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Flights)
admin.site.register(FlightDetails)
admin.site.register(DestinationCities)
admin.site.register(ArrivalCities)
admin.site.register(ReservationDetails)
