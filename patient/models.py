from django.db import models

# Create your models here.

class Patient(models.Model):
    patient_email=models.CharField(max_length=500)
    patient_password=models.CharField(max_length=500)
    patient_name=models.CharField(max_length=500)
    patient_gender=models.CharField(max_length=400)
    patient_age=models.IntegerField()
    patient_phone_number=models.IntegerField()
