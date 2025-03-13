from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'transport_type', 'destination', 'departure_date', 'return_date', 
            'passengers', 'travel_class', 'name', 'email', 'phone'
        ]
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'}),
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
        }
