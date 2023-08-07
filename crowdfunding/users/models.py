

# crowdfunding/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    skills = models.CharField(max_length=15, blank=True, null=True)
    
    AVAILABILITY_CHOICES = (
        ('flexible', 'flexible'),
        ('evenings', 'evenings'),
        ('mornings', 'mornings'),
        ('weekends', 'weekends'),
        ('not_currently_available', 'currently unavailable but pop me on the list'),
        ('busy', 'busy'),
        ('unavailable', 'unavailable'),

        # Add more choices as needed
    )

    availability = models.CharField(max_length=200, choices=AVAILABILITY_CHOICES)


    # pass ???
    def __str__(self):
        return self.username

