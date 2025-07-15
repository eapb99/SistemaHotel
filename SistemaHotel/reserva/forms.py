
from django import forms
from .models import Hotel, Room

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
        widgets = {
            'hotel_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'stars_rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['hotel', 'room_type', 'code', 'is_available']
        widgets = {
            'hotel': forms.Select(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }