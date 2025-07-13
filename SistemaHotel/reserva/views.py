from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import *

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hoteles':hotels} )



def hotel_detail(request,id):
    hotel = Hotel.objects.get(pk = id)
    rooms = Room.objects.filter(hotel=hotel)
    return render(request, 'hotel_detail.html',{'hotel':hotel,'rooms':rooms})