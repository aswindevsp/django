from django.db import models

# Create your models here.
class Doctor(models.Model):
    username = models.CharField(max_length=100,default="doctor")
    password = models.CharField(max_length=100, default="doctor")
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    speciality = models.CharField(max_length=100)
    experience = models.IntegerField()
    qualification = models.CharField(max_length=100)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)