import os
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
# Create your models here.
class CustomUser(AbstractUser):

    

    class GenderChoices(models.TextChoices):
        MALE = 'm'
        FEMALE = 'f'
        OTHER = 'ot'

    phone_number = models.BigIntegerField()
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, default=GenderChoices.MALE)
    

    REQUIRED_FIELDS = ['phone_number']

    def __str__(self) -> str:
        return self.username
    
    def get_absolute_url(self):
        return reverse("home")

