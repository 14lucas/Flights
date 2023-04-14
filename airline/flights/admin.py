from django.contrib import admin


from .models import Flights, Airport, Passanger

#to display description of the flights
class FlightsAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

#to get full description of the passenger include the flights he's in and not
class PassangerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

# Register your models here.

admin.site.register(Airport)
admin.site.register(Flights, FlightsAdmin)
admin.site.register(Passanger, PassangerAdmin)
