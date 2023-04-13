from django.contrib import admin


from .models import Flights, Airport

# Register your models here.

admin.site.register(Airport)
admin.site.register(Flights)
