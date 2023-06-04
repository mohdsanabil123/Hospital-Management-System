from django.db import models

# Create your models here.

class Appointment( models.Model ):
    
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()