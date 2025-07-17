from django.urls import path
from .views import *


urlpatterns = [
    path('', hotel_list, name='hotel_list'),
    path('hotel/<int:id>',hotel_detail,name='hotel_detail'),
    path('hotel/create/', hotel_create, name='hotel_create'),
    path('hotel//delete/<int:id>/', hotel_delete, name='hotel_delete'),
    path('hotel/update/<int:pk>/', hotel_update, name='hotel_update'),
    path('room/list/', room_list, name='room_list'),
    path('room/create/', room_create, name='room_create'),
    path('room/delete/<int:id>/', room_delete, name='room_delete'),
    path('room/update/<int:pk>/', room_update, name='room_update'),
]
