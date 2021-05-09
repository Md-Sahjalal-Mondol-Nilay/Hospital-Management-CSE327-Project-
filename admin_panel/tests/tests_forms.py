from django.test import SimpleTestCase
from admin_panel.forms import DoctorForm,PatientForm

class TestForms(SimpleTestCase):

    def test_DoctorForm_valid_data(self):
        form= DoctorForm(data={
            'doctor_email': 'email1@gmail.com',
            'doctor_password': '1234',
            'doctor_name': 'Amir Khan',
            'doctor_gender': 'Male',
            'doctor_visitng_hour': 'Monday, Tuesday',
            'doctor_room_number': 'LIB611',

        })
    
    def test_PatientForm_valid_data(self):
        form= PatientForm(data={
            'patient_email': 'emai45651@gmail.com',
            'doctor_password': '1456234',
            'patient_name': 'Amir Khannn',
            'patient_gender': 'Male',
            'patient_age': 15,
            'patient_phone_number': 1723333,

        })
    



    
    
    
    
   
   
