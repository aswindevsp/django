from django.db import models

# Create your models here.
class Doctor(models.Model):
    username = models.CharField(max_length=100, default="doctor")
    password = models.CharField(max_length=100,default="doctor")  
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)  
    speciality = models.CharField(max_length=100)
    experience = models.IntegerField()  
    qualification = models.CharField(max_length=100) 

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    doctorname = models.CharField(max_length=20,default="ftdf")
