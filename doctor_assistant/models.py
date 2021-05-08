from django.db import models
from doctor.models import Doctor

# Create your models here.

class DoctorAssistant(models.Model):
    doctor_email= models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor_assistant_email=models.CharField(max_length=500)
    doctor_assistant_password=models.CharField(max_length=500)
    doctor_assistant_name=models.CharField(max_length=500)
    doctor_assistant_gender=models.CharField(max_length=500)
    doctor_assistant_age=models.IntegerField()