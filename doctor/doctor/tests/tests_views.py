from django.test import TestCase, Client
from django.urls import reverse
from doctor.models import Doctor
from django.urls import path, re_path
import json

class TestView(TestCase):

    def setUp(self): # Check every single test method.
        self.client=Client()
        
    
    def test_doctor_authenticatione_GET(self):
        response = self.client.get(reverse('doctor:doctor_authentication')) 
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'doctor/doctor_authentication.html')

    def test_doctor_signup_GET(self):
        response = self.client.get(reverse('doctor:doctor_signup')) 
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'doctor/doctor_signup.html')

    def test_doctor_login_GET(self):
        response = self.client.get(reverse('doctor:doctor_login')) 
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'doctor/doctor_login.html')