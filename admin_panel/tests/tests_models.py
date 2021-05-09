from django.test import TestCase
from doctor.models import Doctor
from patient.models import Patient

class TestModels(TestCase):

    def test_model_Doctor(self):
        doctor_email=Doctor.objects.create(doctor_email="sahjalal.nilay@northsouth.edu")
        doctor_password=Doctor.objects.create(doctor_password="1234")
        doctor_name=Doctor.objects.create(doctor_name="Shahruk Khan")
        doctor_gender=Doctor.objects.create(doctor_gender="Male")
        doctor_visitng_hour=Doctor.objects.create(doctor_visitng_hour="Saturday,Sunday")
        doctor_room_number=Doctor.objects.create(doctor_room_number="ST5002")
    


    def test_model_patient(self):
        patient_email=Patient.objects.create(patient_email="sahjalal1.nilay@northsouth.edu")
        patient_password=Patient.objects.create(patient_password="1234")
        patient_name=Patient.objects.create(patient_name="Salman Khan")
        patient_gender=Patient.objects.create(patient_gender="Male") 
        #patient_age=Patient.objects.create(patient_age=1234)
        #patient_phone_number=Patient.objects.create(patient_phone_number=4566)
       
        # Here Showing Not Null Constraints Error.

        
        
        

