from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_email=models.CharField(max_length=500)
    doctor_password=models.CharField(max_length=500)
    doctor_name=models.CharField(max_length=500)
    doctor_gender=models.CharField(max_length=400)
    doctor_visitng_hour=models.CharField(max_length=400)
    doctor_room_number=models.CharField(max_length=400)

def __str__(self):
    return str(self.pk)+" "+self.doctor_name + " "