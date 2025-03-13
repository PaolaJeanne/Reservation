from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Champ obligatoire et unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Champ numéro de téléphone
    address = models.TextField(blank=True, null=True)  # Champ adresse
    
    def __str__(self):
        return self.username
