from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .forms import ReservationForm
from .models import Reservation


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Remplacez "home" par le nom de votre URL de redirection
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



