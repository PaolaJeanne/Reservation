
import stripe
from django.conf import settings
from django.shortcuts import redirect, render
from Backend.service.forms import ReservationForm
from .models import Service, Payment

# Create your views here.

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service/service_list.html', {'services': services})


stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        # Crée une session Stripe
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'fcfa',
                        'product_data': {
                            'name': service.name,
                        },
                        'unit_amount': int(service.price * 100),  # Prix en centimes
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/services/success/',
            cancel_url='http://127.0.0.1:8000/services/cancel/',
        )
        return redirect(checkout_session.url, code=303)

    return render(request, 'service/payment.html', {'service': service})

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('payment', reservation_id=reservation.id)  # Redirige vers la page de paiement
    else:
        form = ReservationForm()
    return render(request, 'service/reservation_form.html', {'form': form})