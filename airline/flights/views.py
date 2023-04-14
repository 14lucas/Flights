from django.shortcuts import render
from .models import Flights
from django.urls import include
from .models import Passanger
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request, 'flights/index.html',{
        "flights": Flights.objects.all()
    })

def flight(request, flight_id):
    flight = Flights.objects.get(pk = flight_id)
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passangers": flight.passangers.all(),
        "non_passangers": Passanger.objects.exclude(flights = flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flights.objects.get(pk = flight_id)
        passanger = Passanger.objects.get(pk = int(request.POST["passanger"]))
        passanger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args = (flight.id,)))