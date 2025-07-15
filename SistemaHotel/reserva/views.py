from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from .forms import *

# Create your views here.
from .models import *


def hotel_list(request):
    hoteles_list = Hotel.objects.all().order_by('hotel_id')
    paginator = Paginator(hoteles_list, 5)  # 5 hoteles por página
    page = request.GET.get('page')
    hoteles = paginator.get_page(page)
    return render(request, 'hotel_list.html', {'hoteles': hoteles})


def hotel_detail(request,id):
    hotel = Hotel.objects.get(pk = id)
    rooms = Room.objects.filter(hotel=hotel)
    return render(request, 'hotel_detail.html',{'hotel':hotel,'rooms':rooms})


def hotel_create(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
    else:
        form = HotelForm()
    return render(request, 'hotel_create.html', {'form': form})


def hotel_delete(request, id):
    hotel = Hotel.objects.get(pk=id)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotel_list')
    

def hotel_update(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotel_create.html', {'form': form, 'form_title': 'Editar Hotel'})



def room_list(request):
    rooms = Room.objects.select_related('hotel', 'room_type').order_by('room_id')
    paginator = Paginator(rooms, 5)  # 5 habitaciones por página
    page = request.GET.get('page')
    rooms = paginator.get_page(page)
    return render(request, 'room_list.html', {'rooms': rooms})


def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'room_create.html', {'form': form, 'form_title': 'Nueva Habitación'})

def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room_create.html', {'form': form, 'form_title': 'Editar Habitación'})

def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')