# models.py
from django.db import models

class UserProfile(models.Model):
    gender = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timezone_offset = models.CharField(max_length=10)
    timezone_description = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=150)
    password_hash = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    cell = models.CharField(max_length=20)
    ssn = models.CharField(max_length=20, null=True, blank=True) 
    picture_url = models.URLField()
    nationality = models.CharField(max_length=5)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
