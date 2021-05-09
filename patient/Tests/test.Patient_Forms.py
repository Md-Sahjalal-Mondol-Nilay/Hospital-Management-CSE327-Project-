from django import forms
from django import PatientRegisterForm
from django import PatientLoginForm
from patient import models
from django.test import TestCase

class TestRPatientRegisterForm(TestCase):               #test Patient_Register_Form

    def test_PatientRegisterForm_valid_data(self):
        form= PatientForm(data={
            'patient_email': 'email2222@gmail.com',
            'patient_password': '190876543A',
            'patient_name': 'Aliya_Ahmed',
            'patient_gender': 'Female',
            'patient_age': 19,
            'patient_phone_number': 17673333,

        })

    self.assertTrue(form.is_valid())
    
    def test_PatientRegisterForm_no_data(self):
        form = PatientRegisterForm(data={})

        self.assertFalse(form.is_valid())


class TestRPatientLoginForm(TestCase):                  #test Patient_Login_Form

    def test_PatientLoginForm_valid_data(self):
        form= PatientForm(data={
            'patient_email': 'email2222@gmail.com',
            'patient_password': '190876543A',   

        })

    self.assertTrue(form.is_valid())
    
    def test_PatientLoginForm_no_data(self):
        form = PatientRegisterForm(data={})

        self.assertFalse(form.is_valid())
        
