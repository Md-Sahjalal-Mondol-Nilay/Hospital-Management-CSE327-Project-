from django.db import models
from doctor.models import Doctor
from patient.models import Patient

# Create your models here.

class Appointment(models.Model):
    doctor_email= models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_email= models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_serial=models.IntegerField()
    appointment_date=models.CharField(max_length=500)
    appointment_time=models.CharField(max_length=500)
    appointment_room_number=models.CharField(max_length=500)




