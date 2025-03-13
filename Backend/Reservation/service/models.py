from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', blank=True, null=True)  # Optionnel

    def __str__(self):
        return self.name


class Payment(models.Model):
    service = models.ForeignKey('Service', on_delete=models.CASCADE)  # Associe le paiement à un service
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paiement de {self.amount} FCFA pour {self.service.name}"


class Reservation(models.Model):
    TRANSPORT_CHOICES = [
        ('terrestre', 'Transport Terrestre'),
        ('aerien', 'Transport Aérien'),
        
    ]

    transport_type = models.CharField(max_length=20, choices=TRANSPORT_CHOICES)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)  # Optionnel pour le terrestre
    passengers = models.PositiveIntegerField()
    travel_class = models.CharField(max_length=50, blank=True, null=True)  # Aérien uniquement
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.destination} ({self.transport_type})"
